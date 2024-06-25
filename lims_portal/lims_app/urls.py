from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views, admin

urlpatterns = [
    path('add-books/', views.add_books, name='add_books'),
    path('home/', views.Home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('staff/', views.Staff, name='Staff'),
    path('catalogue/', views.catalogue, name='catalogue'),
    #path('user/', views.user, name='user'),
    path('contact/', views.contact, name='contact'),
    path('about us/', views.about_us, name='about us'),
    path('userlogout/', views.user_logout, name='userlogout'),
    path('services/', views.services, name='services'),
    path('select-redirect/', views.select_redirect, name='select_redirect'),
    path('search-books/', views.search_books, name='search_books'),
    path('book/<int:id>/', views.book_profile, name='book_profile'),
    path('user/', views.search_books, name='user_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
