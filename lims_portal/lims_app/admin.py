from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AddBook, profile
from django.contrib.auth.models import User

admin.site.register(AddBook)

class ProfileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'profile'


class CustomizedUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)

