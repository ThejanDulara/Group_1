from django.shortcuts import render, redirect
from .forms import AddBookForm
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


def Staff(request):
    return render(request, 'lims_app/staff_page.html')


def catalogue(request):
    return render(request, 'lims_app/catalogue.html')


@login_required(login_url="login")
def user(request):
    return render(request, 'lims_app/user_page.html')


def contact(request):
    return render(request, 'lims_app/contact.html')


def about_us(request):
    return render(request, 'lims_app/about_us.html')


def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("user")

    context = {'loginform': form}

    return render(request, 'lims_app/login.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user")  # Redirect to user page after successful registration
    else:
        form = CreateUserForm()

    context = {'signupform': form}
    return render(request, 'lims_app/register.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("home")
