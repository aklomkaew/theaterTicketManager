from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# from django import Template
from . import models
import datetime




def index(request) :
    return render(request, 'webapp/home.html')

def getPerformances(request, theater, month, day, year):


    my_theater = ['ConcertHall', 'Playhouse']
    theater = 'concertHall'
    season = 'Spring'
    day = '11-12-18'
    performances_list = []
    summaryString = "Don't waste your time with this one!"
    showtime_one = {}
    showtime_two = {}
    showtime_one['hour'] = 5
    showtime_one['minute'] = 30
    showtime_one['str'] = '5:30'
    showtime_two['hour'] = 6
    showtime_two['minute'] = 15
    showtime_two['str'] = '6:30'
    showtimes = [showtime_one, showtime_two]
    johnPrine = { 'name': 'John Prine', 'img': 'img/johnPrine.png', 'runtime': '4hrs. 1 min.', 'genre': 'Tragedy', 'summary': summaryString, 'showtimes':showtimes, 'theater': theater, 'season': season, 'month':'11','day': '16', 'year': '2018', 'showtimes': showtimes}
    scotty = { 'name': 'Scotty McCreedy', 'img': 'img/scottyMcCreedy.png', 'runtime': '3hrs. 1 min.', 'genre': 'Drama', 'summary': summaryString, 'showtimes':showtimes, 'theater': theater, 'season': season, 'month':'11','day': '16', 'year': '2018', 'showtimes': showtimes}
    performances_list.append(johnPrine)
    #performances_list.append(scotty)
    context = {
        'theaters': my_theater,
        'performances': performances_list
    }
    return render(request, 'webapp/performanceCards.html', context)

def performance(request) :
    #Build a list of the Theaters from the database
    theaters = []

    for each in models.Theater.objects.all():
        theaters.append(str(each))


    theater = 'concertHall'

    performances_list = []

    #Iterate through each Show and build data for it
    for show in models.Show.objects.all():

        #Build a list of showtimes
        showtimes = []

        #Used for getting the name of the theater for this show
        theater= ""

        #Build a list of showtimes, each containing a dict with hour, minute, and string representation of that.
        for performance in show.performances.all():

            #Assume that all performances are in the same theater, so only check once
            if theater == "":
                theater = str(performance.theater)

            showtime  = {}
            showtime['hour'] = int(performance.time.hour)
            showtime['minute'] = int(performance.time.minute)
            showtime['str'] = str(performance.time.hour) + ':' + str(performance.time.minute)
            showtimes.append(showtime)

        show = { 'name': str(show.name), 'img': (show.img), 'runtime': str(show.runtime), 'genre': str(show.genre), 'summary': str(show.summary), 'showtimes':showtimes, 'theater': theater, 'season': show.get_season(), 'month':'11','day': '16', 'year': '2018', 'showtimes': showtimes}
        performances_list.append(show)

    context = {'theaters': theaters, 'performances': performances_list}

    return render(request, 'webapp/performance.html', context)

def contact(request) :
    return render(request, 'webapp/contact.html')

def admin(request) :
    return render(request, 'webapp/admin.html')

def payment(request, theater, year, month, day, hour, minute, seats) :
    seats_list = seats.split(',')
    sorted_seats_list = seats_list.sort()
    context = {}
    context['theater'] = theater
    context['year'] = year
    context['month'] = month
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    context['seats'] = sorted_seats_list
    context['seat_str'] = seats
    return render(request, 'webapp/payment.html', context)

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
# <str:theater>/<str:year>/<str:day>/<str:hour>/<str:minute>/

def seatSelection(request, theater, year=None, month=None, day=None, hour=None, minute=None):
    context = {}
    context['theater'] = theater
    context['year'] = year
    context['month'] = month
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    return render(request, 'webapp/seatSelection.html', context)

def concertHall(request, theater, year, month, day, hour, minute):
    # SHAWN, year, month, day, hour, minute are currently ints
    # str(year) is all you have to do to get them back to strings


    """Find all of the sold seats. Use every seat that is sold as a key to a dictionary. """

    # Create the initial set of seats and mark them all available.
    context = populateConcertHallSeats()

    # Assume we are using the Concert Hall theater
    theater = models.Theater.objects.get(name="Concert Hall")

    # build a datetime object to use for comparison
    date = datetime.date(year, month, day)

    # Iterate through every Performance in that theater
    for performance in theater.performance_set.all():

        # Check for one that matches the specified date and time
        # There should only be ONE performance that meets these criteria
        if performance.time.date() == date and performance.time.hour == hour and performance.time.minute == minute:

            # Get the set of tickets that refer to this performance
            tickets = performance.ticket_set.all()

            # Iterate through the tickets for this performance
            for ticket in tickets:
                # Mark the ticket as sold.
                context[str(ticket.row.all()[0]) + str(ticket.seat.all()[0])] = 'sold'

        # Go ahead and return, since we have dealt with the ONE performance at the specific date and time.
        return render(request, 'webapp/concertHall.html', context)

def confirmationPage(request, theater, year, month, day, hour, minute, seats, paid):
    context = {}
    context['theater'] = theater
    context['year'] = year
    context['month'] = month
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    context['seats'] = seats
    context['paid'] = paid
    test_str = theater + "---" + str(year) + "---" + str(month) + "---" + str(day) + "---" + str(hour) + "---" + str(minute) + "---" + seats + "---" + paid
    return HttpResponse(test_str)

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
