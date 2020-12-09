from django.urls import path
from storage import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users')
]
