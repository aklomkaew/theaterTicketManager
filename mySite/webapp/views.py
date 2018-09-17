from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return render(request, 'webapp/home.html')

def theater(request) :
    return render(request, 'webapp/theater.html')

def performance(request) :
    return render(request, 'webapp/performance.html')
