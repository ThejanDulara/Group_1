from django.db import models


class AddBook(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rack_number = models.CharField(max_length=50)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Register(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='other')

    def __str__(self):
        return self.username

