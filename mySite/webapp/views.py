from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Ticket

from webapp.forms import TicketsForm


def index(request) :
    return render(request, 'webapp/home.html')

def theater(request) :
    return render(request, 'webapp/theater.html')

def performance(request) :
    """if request.method == 'POST':
        form = TicketsForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = TicketsForm()

    #Create a database entry
    ticket = Ticket(name="test", seat="test", show="test", season = 1, play=1, date= "2010-01-26 09:20", paid= True, door = True)
    ticket.save()

    #Print the value of that database entry.
    seat = Ticket.objects.filter(name="test").values('seat')


    return render(request, 'webapp/performance.html', {'seat': seat})"""
    return render(request, 'webapp/performance.html')
