from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! This is the home page of my Django app.")