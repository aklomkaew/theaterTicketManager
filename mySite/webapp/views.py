from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

def index(request) :
    return render(request, 'webapp/home.html')

def performance(request) :
    return render(request, 'webapp/performance.html')

def contact(request) :
    return render(request, 'webapp/contact.html')

def buySeasonTicket(request) :
    return render(request, 'webapp/buySeasonTicket.html')

def admin(request) :
    return render(request, 'webapp/admin.html')

def payment(request) :
    return render(request, 'webapp/payment.html')

def seatSelection(request):
    context = {}
    # Row A
    for i in range(1,37):
        key = 'A' + str(i)
        context[key] = 'available'
    # Row B
    for i in range(1,39):
        key = 'B' + str(i)
        context[key] = 'available'
    # Row C
    for i in range(1,43):
        key = 'C' + str(i)
        context[key] = 'available'
    context['A16'] = 'sold'
    context['A17'] = 'sold'
    context['A18'] = 'sold'
    return render(request, 'webapp/seatSelection.html', context)

def confirmationPage(request, seat_numbers):
    return HttpResponse(seat_numbers)
