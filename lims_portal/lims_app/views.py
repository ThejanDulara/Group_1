from django.shortcuts import render, redirect
from .forms import AddBookForm


def add_books(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_books')  # Redirect to the same page after saving
    else:
        form = AddBookForm()

    return render(request, 'lims_app/add_books.html', {'form': form})


def landing_page(request):
    """if request.method == 'POST':
        form = LanfingPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_books')  # Redirect to the same page after saving
    else:
        form = AddBookForm()"""

    return render(request, 'lims_app/landing_page.html')

def Register(request):
    """if request.method == 'POST':
        form = LanfingPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_books')  # Redirect to the same page after saving
    else:
        form = AddBookForm()"""

    return render(request, 'lims_app/Registration.html')

def Login(request):
    """if request.method == 'POST':
        form = LanfingPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_books')  # Redirect to the same page after saving
    else:
        form = AddBookForm()"""

    return render(request, 'lims_app/Login.html')
