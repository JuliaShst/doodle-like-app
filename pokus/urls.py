from django.urls import path
from pokus import views

app_name = 'pokus'

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("base/", views.base, name="base"),
    path("add_new/", views.add_new, name="add_new"),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path("logout", views.logout_request, name= "logout"),

]