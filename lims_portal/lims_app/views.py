from django.shortcuts import render, redirect
from .forms import AddBookForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


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


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegisterForm()  # No initial data

    return render(request, 'lims_app/Registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = request.POST.get('login-type')  # Assuming you have a login-type field in your form

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user_type == 'staff':
                    return redirect('Staff')  # Redirect to staff page
                elif user_type == 'member':
                    return redirect('user')  # Redirect to member page
            else:
                messages.error(request, 'Invalid username or password.')

    else:
        form = LoginForm()

    return render(request, 'lims_app/login.html', {'form': form})


def Staff(request):
    return render(request, 'lims_app/staff_page.html')


def catalogue(request):
    return render(request, 'lims_app/catalogue.html')


def user(request):
    return render(request, 'lims_app/user_page.html')


def contact(request):
    return render(request, 'lims_app/contact.html')
