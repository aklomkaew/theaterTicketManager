from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# from django import Template
from . import models
import datetime




def index(request) :
    return render(request, 'webapp/home.html')

"""Called when the user clicks 'View Shows' on the Performances page.
    Gets the set of shows and performances subject to the filters provided by the user.
    Returns them in a format that can be used to generate cards."""
def getPerformances(request, theater, month, day, year):

    #Build a list of dictionaries containing details of each show
    showDetails = []

    # Create a datetime.date object for the day of the year
    date = datetime.date(int(year), int(month), int(day))

    # Get the set of shows
    shows = models.Show.objects.all()

    # Filter for shows that have performances that are on the specified day
    for show in shows:

        # A sentinal value for keeping track of whether this show is relevant to our filters at all
        relevant = False

        theaterName = "Concert Hall"
        # Build a list of showtimes
        showtimes = []

        # Iterate through the performances in this show
        for performance in show.performances.all():

            # Check if the current performance is on the right day of the year
            #Also, check that it is in the selected theater
            if performance.time.date() == date and str(performance.theater.all()[0]) == theater:

                relevant = True

                # Get the name of the theater for this performance
                # Assume that all performances are in the same theater
                theaterName = str(performance.theater.all()[0].name)

                # Use hardcoded values to interpret which part of the website to call
                if theaterName == "Concert Hall":
                    theaterName = 'concertHall'
                elif theaterName == "Playhouse Theater":
                    theaterName = 'playhouse'

                showtime = {}
                showtime['hour'] = int(performance.time.hour)
                showtime['minute'] = int(performance.time.minute)
                showtime['str'] = str(performance.time.hour) + ':' + str(performance.time.minute)
                showtimes.append(showtime)

        # We now have list of the relevant performances

        # Ensure that we only reply with details of this show if it is relevant
        if relevant == True:

            # showtimes is only the showtimes that are on this day

            # Build a response dictionary to send back
            dict = {'name': str(show.name),
                    'img': str(show.img),
                    'runtime': str(show.runtime),
                    'genre': str(show.genre),
                    'summary': str(show.summary),
                    'season': str(show.get_season()),
                    'showtimes': showtimes,
                    'theater': theaterName,
                    'month': str(month),
                    'day': str(day),
                    'year': str(year),
                    }

            # Add this response dictionary to the list of responses
            showDetails.append(dict)

    # Build the context
    context = {
        'theaters': list(theater),
        'performances': showDetails
    }

    return render(request, 'webapp/performanceCards.html', context)

"""Called when the the Performances page is visited."""
def performance(request) :
    # Input values for the default set of cards
    # Default is to display showings for Concert Hall today
    theater = "Concert Hall"
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day

    #Build a list of the Theaters from the database
    theaters = []

    for each in models.Theater.objects.all():
        theaters.append(str(each))


    # Build a list of dictionaries containing details of each show
    showDetails = []

    # Create a datetime.date object for the day of the year
    date = datetime.date(int(year), int(month), int(day))

    # Get the set of shows
    shows = models.Show.objects.all()

    # Filter for shows that have performances that are on the specified day
    for show in shows:

        # A sentinal value for keeping track of whether this show is relevant to our filters at all
        relevant = False

        theaterName = "Concert Hall"
        # Build a list of showtimes
        showtimes = []

        # Iterate through the performances in this show
        for performance in show.performances.all():

            # Check if the current performance is on the right day of the year
            # Also, check that it is in the selected theater
            if performance.time.date() == date and str(performance.theater.all()[0]) == theater:

                relevant = True

                # Get the name of the theater for this performance
                # Assume that all performances are in the same theater
                theaterName = str(performance.theater.all()[0].name)

                # Use hardcoded values to interpret which part of the website to call
                if theaterName == "Concert Hall":
                    theaterName = 'concertHall'
                elif theaterName == "Playhouse Theater":
                    theaterName = 'playhouse'

                showtime = {}
                showtime['hour'] = int(performance.time.hour)
                showtime['minute'] = int(performance.time.minute)
                showtime['str'] = str(performance.time.hour) + ':' + str(performance.time.minute)
                showtimes.append(showtime)

        # We now have list of the relevant performances

        # Ensure that we only reply with details of this show if it is relevant
        if relevant == True:
            # showtimes is only the showtimes that are on this day

            # Build a response dictionary to send back
            dict = {'name': str(show.name),
                    'img': str(show.img),
                    'runtime': str(show.runtime),
                    'genre': str(show.genre),
                    'summary': str(show.summary),
                    'season': str(show.get_season()),
                    'showtimes': showtimes,
                    'theater': theaterName,
                    'month': str(month),
                    'day': str(day),
                    'year': str(year),
                    }

            # Add this response dictionary to the list of responses
            showDetails.append(dict)

    context = {'theaters': theaters, 'performances': showDetails}

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
