from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'demo_site.html')
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")

    
