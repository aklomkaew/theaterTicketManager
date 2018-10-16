from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return render(request, 'webapp/home.html')

def performance(request) :
    return render(request, 'webapp/performance.html')

def contact(request) :
    return render(request, 'webapp/contact.html')

def buySeasonTicket(request) :
    return render(request, 'webapp/buySeasonTicket.html')

def payment(request) :
    return render(request, 'webapp/payment.html')
