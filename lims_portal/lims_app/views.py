from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
from .models import *
# from .forms import *
from .forms import StudentProfileForm, UserRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden