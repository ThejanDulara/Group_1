from django import forms
from .models import AddBook, profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    fullname = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=profile.GENDER_CHOICES, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'fullname', 'phone_number', 'gender']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
            profile_instance = profile.objects.create(
                user=user,
                fullname=self.cleaned_data['fullname'],
                phone_number=self.cleaned_data['phone_number'],
                gender=self.cleaned_data['gender']
            )
            profile_instance.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())