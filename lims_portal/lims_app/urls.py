from django.urls import path
from . import views

urlpatterns = [
    path('Add Books/', views.add_books, name='add_books'),
    path('Home/', views.Home, name='Home'),
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('Staff/', views.Staff, name='Staff'),
]


