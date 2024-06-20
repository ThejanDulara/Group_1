from django import forms
from .models import AddBook

class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ['name', 'author', 'rack_number', 'category', 'quantity', 'description']
