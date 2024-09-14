from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user
        
class ActionForm(forms.Form):
    title = forms.CharField(max_length=100)
    description  =forms.CharField(widget=forms.Textarea)
    duration = forms.IntegerField(min_value=10, max_value=180, initial=60, widget=forms.TextInput(attrs={'type': 'range', 'step': '10'}))

    date_time_options_1 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_2 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,

    )

    date_time_options_3 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_4 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_5 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_6 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_7 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_8 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_9 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    date_time_options_10 = forms.DateTimeField(
        label='Date and Time options',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False,
    )

    


