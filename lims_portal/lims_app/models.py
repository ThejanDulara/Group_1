from django.db import models

class AddBook(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rack_number = models.CharField(max_length=50)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()

