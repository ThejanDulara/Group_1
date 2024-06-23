from django.urls import path
from . import views, admin

urlpatterns = [
    path('add-books/', views.add_books, name='add_books'),
    path('home/', views.Home, name='Home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('staff/', views.Staff, name='Staff'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('user/', views.user, name='user'),
    path('contact/', views.contact, name='contact'),
    path('about us/', views.about_us, name='about us'),
]

