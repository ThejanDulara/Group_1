from django.shortcuts import render, redirect
from .forms import AddBookForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile


def add_books(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_books')  # Redirect to the same page after saving
    else:
        form = AddBookForm()

    return render(request, 'lims_app/add_books.html', {'form': form})


def Home(request):
    return render(request, 'lims_app/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'lims_app/register.html', {'form': form})


def profile(request):
    if request.user.groups.filter(name='Staff').exists():
        return redirect('staff')
    else:
        return redirect('user')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                profile = Profile.objects.get(user=user)
                if profile.user_type == 'staff':
                    return redirect('Staff')
                elif profile.user_type == 'member':
                    return redirect('user')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'lims_app/login.html', {'form': form})


def Staff(request):
    return render(request, 'lims_app/staff_page.html')


def catalogue(request):
    return render(request, 'lims_app/catalogue.html')


def user(request):
    return render(request, 'lims_app/user_page.html')


def contact(request):
    return render(request, 'lims_app/contact.html')


def about_us(request):
    return render(request, 'lims_app/about_us.html')
