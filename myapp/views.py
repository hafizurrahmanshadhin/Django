from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello! This is the home page of my Django app.")


def profile(request):
    return HttpResponse("This is the profile page of my Django app.")


def dashboard(request):
    return HttpResponse("Welcome to the dashboard of my Django app.")


def about(request):
    return render(request, "about.html")
