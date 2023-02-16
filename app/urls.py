from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
	path(r'home/', views.main, name='main'),
	path(r'info/', views.users, name='users'),
	path(r'signup', views.sign_up_form, name='signup'),
]
