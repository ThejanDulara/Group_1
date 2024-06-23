from django.contrib.auth.models import User
from django.db import models


class AddBook(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rack_number = models.CharField(max_length=50)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()


class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('member', 'Member'),
        ('staff', 'Staff'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='other')
    user_type = models.CharField(max_length=6, choices=USER_TYPE_CHOICES, default='member')



