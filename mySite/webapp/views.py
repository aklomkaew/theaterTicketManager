from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# from django import Template
from . import models



def index(request) :
    return render(request, 'webapp/home.html')

def getPerformances(request, theater, month, day, year) :
    my_theater = ['ConcertHall', 'Playhouse']
    theater = 'ConcertHall'
    season = 'Spring'
    day = '11-12-18'
    performances_list = []
    summaryString = "Don't waste your time with this one!"
    showtimes = ['5:00', '7:00','9:00','11:00']
    johnPrine = { 'name': 'John Prine', 'img': '/img/johnPrine.png', 'runtime': '4hrs. 1 min.', 'genre': 'Tragedy', 'summary': summaryString, 'showtimes':showtimes, 'theater': theater, 'season': season, 'day': day }
    scotty = { 'name': 'Scotty McCreedy', 'img': '/img/scottyMcCreedy.png', 'runtime': '3hrs. 1 min.', 'genre': 'Drama', 'summary': summaryString, 'showtimes':showtimes, 'theater': theater, 'season': season, 'day': day }
    performances_list.append(johnPrine)
    # performances_list.append(scotty)
    context = {
        'theaters': my_theater,
        'performances': performances_list
    }
    return render(request, 'webapp/performanceCards.html', context)

def performance(request) :
    my_theater = ['ConcertHall', 'Playhouse']
    theater = 'ConcertHall'
    season = 'Spring'
    day = '11-12-18'
    performances_list = []
    summaryString = "Don't waste your time with this one!"
    showtimes = ['5:00', '7:00','9:00','11:00']
    johnPrine = { 'name': 'John Prine', 'img': '/img/johnPrine.png', 'runtime': '4hrs. 1 min.', 'genre': 'Tragedy', 'summary': summaryString, 'showtimes':showtimes, 'theater': theater, 'season': season, 'day': day }
    scotty = { 'name': 'Scotty McCreedy', 'img': '/img/scottyMcCreedy.png', 'runtime': '3hrs. 1 min.', 'genre': 'Drama', 'summary': summaryString, 'showtimes':showtimes, 'theater': theater, 'season': season, 'day': day }
    performances_list.append(johnPrine)
    performances_list.append(scotty)
    context = {
        'theaters': my_theater,
        'performances': performances_list
    }
    return render(request, 'webapp/performance.html', context)

def contact(request) :
    return render(request, 'webapp/contact.html')

def admin(request) :
    return render(request, 'webapp/admin.html')

def payment(request) :
    return render(request, 'webapp/payment.html')

def populateConcertHallSeats():
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
    for i in range(1,43):
        key = 'D' + str(i)
        context[key] = 'available'
    for i in range(1,45):
        key = 'E' + str(i)
        context[key] = 'available'
    for i in range(1,39):
        key = 'F' + str(i)
        context[key] = 'available'
    for i in range(1,29):
        key = 'G' + str(i)
        context[key] = 'available'
    for i in range(1,29):
        key = 'H' + str(i)
        context[key] = 'available'
    for i in range(1,49):
        key = 'I' + str(i)
        context[key] = 'available'
    for i in range(1,59):
        key = 'J' + str(i)
        context[key] = 'available'
    for i in range(1,53):
        key = 'K' + str(i)
        context[key] = 'available'
    for i in range(1,53):
        key = 'L' + str(i)
        context[key] = 'available'
    for i in range(1,55):
        key = 'M' + str(i)
        context[key] = 'available'
    for i in range(1,59):
        key = 'N' + str(i)
        context[key] = 'available'
    for i in range(1,55):
        key = 'O' + str(i)
        context[key] = 'available'
    for i in range(1,47):
        key = 'P' + str(i)
        context[key] = 'available'
    for i in range(1,47):
        key = 'Q' + str(i)
        context[key] = 'available'
    for i in range(1,52):
        key = 'R' + str(i)
        context[key] = 'available'
    for i in range(1,48):
        key = 'S' + str(i)
        context[key] = 'available'
    for i in range(1,61):
        key = 'T' + str(i)
        context[key] = 'available'
    for i in range(1,59):
        key = 'U' + str(i)
        context[key] = 'available'
    for i in range(1,63):
        key = 'V' + str(i)
        context[key] = 'available'
    for i in range(1,59):
        key = 'W' + str(i)
        context[key] = 'available'
    for i in range(1,59):
        key = 'X' + str(i)
        context[key] = 'available'
    for i in range(1,59):
        key = 'Y' + str(i)
        context[key] = 'available'
    for i in range(1,59):
        key = 'Z' + str(i)
        context[key] = 'available'
    return context

def seatSelection(request, theater=None, day=None, time=None):
    return render(request, 'webapp/seatSelection.html')

def concertHall(request, day=None, time=None):
    context = populateConcertHallSeats()
    context['A1'] = 'sold'
    return render(request, 'webapp/concertHall.html', context)

def confirmationPage(request, seat_numbers):
    return HttpResponse(seat_numbers)

def buySeasonTicket(request):
    my_seasons = models.Season.objects.all
    my_theater = models.Theater.objects.all
    context = {
        'seasons': my_seasons,
        'theaters': my_theater
    }

    return render(request, 'webapp/buySeasonTicket.html', context)

def seasonSeatSelection(request, theater, season, day, time):
    str = ''
    str += theater + season + day + time
    return HttpResponse(str)
    # context = {
    #
    # }
    # return render(request, 'webapp/seasonSeatSelection.html')

def seatSelect(request):
    return render(request, 'webapp/seatSelection.html')

def seasonSeatSelect(request):
    return render(request, 'webapp/seasonSeatSelection.html')
