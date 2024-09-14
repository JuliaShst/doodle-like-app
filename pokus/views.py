from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .forms import ActionForm
from .models import Event, DateTimeOption
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'pokus/base.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("pokus:login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()

    return render(
        request=request,
        template_name="pokus/register.html",
        context={"register_form": form},
    )

    
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("pokus:add_new")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="pokus/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	return redirect("pokus:login")


@login_required
def add_new(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            duration = form.cleaned_data['duration']

            event = Event(
                title=title,
                description=description,
                duration=duration,
                created_by=request.user,  # request.user to get the currently logged-in user
                created_at=timezone.now(),
            )
            event.save()

            for i in range(1, 11): 
                date_time_field_name = f'date_time_options_{i}'
                date_time = form.cleaned_data.get(date_time_field_name)
                if date_time:
                    date_time_option = DateTimeOption(date_time=date_time)
                    date_time_option.save()
                    event.date_time_options.add(date_time_option)

            return HttpResponseRedirect(reverse('pokus:event_detail', args=[event.id]))
        
        else:

            messages.error(request, 'Form submission is not valid. Please correct the errors.')

    else:
        form = ActionForm()

    return render(request, 'pokus/add_new.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, DateTimeOption 


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    date_time_options = event.date_time_options.all()

    if request.method == 'POST':
        time_slot_id = request.POST.get('time_slot')  
        user_name = request.POST.get('user_name')

        # Get the selected DateTimeOption
        selected_time_slot = get_object_or_404(DateTimeOption, pk=time_slot_id)

        # Update 
        selected_time_slot.voter_name = user_name
        selected_time_slot.save()

        return redirect('pokus:event_detail', event_id=event.id)

    return render(request, 'pokus/event_detail.html', {'event': event, 'date_time_options': date_time_options})


