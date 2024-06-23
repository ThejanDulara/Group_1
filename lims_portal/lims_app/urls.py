from django.urls import path
from . import views, admin

urlpatterns = [
    path('add-books/', views.add_books, name='add_books'),
    path('home/', views.Home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('staff/', views.Staff, name='Staff'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('user/', views.user, name='user'),
    path('contact/', views.contact, name='contact'),
    path('about us/', views.about_us, name='about us'),
    path('userlogout/', views.user_logout, name='userlogout'),
    path('services/', views.services, name='services'),
]

