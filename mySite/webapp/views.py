from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# from django import Template
from . import models
from . import utility
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

def seasonPayment(request, theater, season, day, hour, minute, seats) :
    seats_list = seats.split(',')
    sorted_seats_list = seats_list.sort()
    context = {}
    context['theater'] = theater
    context['season'] = season
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    context['seats'] = sorted_seats_list
    context['seat_str'] = seats
    return render(request, 'webapp/seasonPayment.html', context)

def payment(request, show, theater, year, month, day, hour, minute, seats) :
    seats_list = seats.split(',')
    sorted_seats_list = seats_list.sort()
    context = {}
    context['show'] = show
    context['theater'] = theater
    context['year'] = year
    context['month'] = month
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    context['seats'] = sorted_seats_list
    context['seat_str'] = seats
    return render(request, 'webapp/payment.html', context)

# <str:theater>/<str:year>/<str:day>/<str:hour>/<str:minute>/

def seatSelection(request, show, theater, year=None, month=None, day=None, hour=None, minute=None):
    context = {}
    context['show'] = show
    context['theater'] = theater
    if theater == "concertHall":
        theater_str = "Concert Hall"
    if theater == "playhouse":
        theater_str = "Playhouse"
    context['theater_str'] = theater_str
    context['year'] = year
    context['month'] = month
    context['day'] = day
    if hour <= 12:
        hour_str = str(hour)
        am_pm_string = "AM"
    else:
        hour_str = str(hour - 12)
        am_pm_string = "AM"
    context['hour'] = hour_str
    context['am_pm_string'] = am_pm_string
    minute_str = minute
    if minute < 10:
        minute_str = '0' + str(minute)
    context['minute_str'] = minute_str
    context['minute'] = minute
    return render(request, 'webapp/seatSelection.html', context)

def seasonConcertHall(request, blank, theater, season, day, hour, minute):
    #Operates generally the same way as concertHall, but seats are marked as sold if a ticket exists for that seat in ANY performance (within criteria) in the season

    # Create the initial set of seats and mark them all available.
    context = populateConcertHallSeats()

    #Get the list of performances that are on the specified weekday in this season
    performances = utility.getPerformancesOnWeekdayInSeason(day, season)

    # Assume we are using the Concert Hall theater
    theater = models.Theater.objects.get(name="Concert Hall")

    for performance in performances:
        # Get the set of tickets that refer to this performance
        tickets = performance.ticket_set.all()

        # Iterate through the tickets for this performance
        for ticket in tickets:
            # Mark the ticket as sold.
            context[str(ticket.row.all()[0]) + str(ticket.seat.all()[0])] = 'sold'


    return render(request, 'webapp/concertHall.html', context)

def concertHall(request, show, theater, year, month, day, hour, minute):
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

def playhouse(request, show, theater, year, month, day, hour, minute):
    # SHAWN, year, month, day, hour, minute are currently ints
    # str(year) is all you have to do to get them back to strings
    context = {}
    return render(request, 'webapp/playhouse.html', context)

    """Find all of the sold seats. Use every seat that is sold as a key to a dictionary. """

    # Create the initial set of seats and mark them all available.
    context = populatePlayhouseSeats()

    # Assume we are using the Concert Hall theater
    theater = models.Theater.objects.get(name="Playhouse Theater")

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
            return render(request, 'webapp/playhouse.html', context)


# path('seasonConfirmationPage/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/<str:seats>/<str:paid>/<str:name>/<str:phoneNumber>/<str:email>/<str:door_reservation>/<str:printed>/<str:payment_method>/', views.season_confirmationPage, name='seasonConfirmationPage'),
def season_confirmationPage(request, theater, season, day, hour, minute, seats, paid, name, address, phoneNumber, email, door_reservation, printed, payment_method):

    # Check if the Customer exists
    nameParts = name.split()

    firstname = ""
    middlename = ""
    lastname = ""

    if theater == 'concertHall':
        theaterName = "Concert Hall"
    elif theater == 'playhouse':
        theaterName = 'Playhouse Theater'

    theaterObject = models.Theater.objects.filter(name=theaterName)

    # Create the variable in this scope for referencing later
    customer = models.Customer(firstName="temp", lastName="temp")

    # TODO: Add error handling for corrupted name
    # Check if a middle name was provided
    if len(nameParts) > 2:
        firstname = nameParts[0]
        middlename = nameParts[1]
        lastname = nameParts[2]

        # Use filter. If len = 1, then the user exists. If not, then create it.

        customers = models.Customer.objects.filter(firstName=firstname, middleName=middlename, lastName=lastname)

        # A record already exists for this customer.
        if len(customers) == 1:
            customer = customers[0]
        elif len(customers) == 0:
            customer = models.Customer(firstName=firstname, middleName=middlename, lastName=lastname, email=email,
                                       phone=phoneNumber, address=address)
            customer.save()

    else:
        firstname = nameParts[0]
        lastname = nameParts[1]

        customers = models.Customer.objects.filter(firstName=firstname, lastName=lastname)

        # A record already exists for this customer.
        if len(customers) == 1:
            customer = customers[0]
        elif len(customers) == 0:
            customer = models.Customer(firstName=firstname, lastName=lastname, email=email, phone=phoneNumber, address=address)
            customer.save()

    # We have the customer, now get the rest of the information we need for creating a ticket.
    # Get a set of seats
    seatObjects = []
    rows = []
    sections = []

    individualSeatParts = seats.split(',')
    for i, part in enumerate(individualSeatParts):
        rows.append(models.Row.objects.get(name=part[0]))
        seatObjects.append(models.Seat.objects.get(number=int(part[1])))

        # Filter through the sections containing this row to find the one that is in the specified theater
        # Find the section that this row is in that is itself in the theater
        for section in rows[i].section_set.all():

            matchingTheaters = section.theater_set.filter(name=theaterName)

            if len(matchingTheaters) == 1:
                sections.append(section)
                break

    performances = utility.getPerformancesOnWeekdayInSeason(day, season)

    print(performances)

    # TODO: Test this logic with a modified Season Ticket selection and payment page.
    #Iterate through each performance in the set of valid performances in the Season
    for performance in performances:

        #Create a ticket for eacb seat in this performace
        for i, seat in enumerate(seatObjects):

            ticket = models.Ticket.objects.create(datePurchased=datetime.datetime.now(), door=bool(door_reservation))
            ticket.paid = bool(paid)

            if bool(paid) == True:
                ticket.cash = bool(payment_method)

            ticket.printed = bool(printed)
            ticket.customer.add(customer)
            ticket.seat.add(seat)
            ticket.row.add(rows[i])
            ticket.section.add(sections[i])

            #Find the Show for this performance.
            #It should be the one that references the performance and is in the appropriate season and theater
            show = ""
            for each in performance.show_set.all():

                if len(each.season_set.filter(name=season)) >= 1 and len(performance.theater.filter(name=theaterName)) >= 1:

                    show = each
                    break

            ticket.season.add(models.Season.objects.get(name=season))
            ticket.show.add(show)
            ticket.performance.add(performance)
            ticket.save()

    #Create a SeasonTicketHolder record for this customer or update an existing one
    #Check if there is already a SeasonTicketHolder for this customer
    if len(customer.seasonticketholder_set.all()) < 1:

        holder = models.SeasonTicketHolder.objects.create(valid=True)
        holder.customer.add(customer)
        holder.seasons.add(models.Season.objects.get(name=season))
        holder.save()
    else:
        holder = customer.seasonticketholder_set.get(customer=customer)
        holder.valid = True

        #Check if this Season does not already exists in the record
        if len(holder.seasons.filter(name=season)) < 1:

            #If that is true, then add the specifid season
            holder.seasons.add(models.Season.objects.get(name=season))

        holder.save()

    context = {}
    context['theater'] = theater
    context['season'] = season
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    context['seats'] = seats
    context['paid'] = paid
    context['name'] = name
    context['phoneNumber'] = phoneNumber
    context['address'] = address
    context['email'] = email
    context['door_reservation'] = door_reservation
    context['printed'] = printed
    context['payment_method'] = payment_method
    test_str = theater + "---" + season + "---" + str(day) + "---" + str(hour) + "---" + str(minute) + "---" + seats + "---" + str(paid) + "---" + name + "---" + phoneNumber + "---" + email + "---" + str(
        door_reservation) + "---" + str(printed) + "---" + str(payment_method)  + "---" + address

    return HttpResponse(test_str)


def confirmationPage(request, show, theater, year, month, day, hour, minute, seats, paid, name, door_reservation, printed, payment_method):
# Check if the Customer exists
    nameParts = name.split()

    firstname = ""
    middlename = ""
    lastname = ""

    if theater == 'concertHall':
        theaterName = "Concert Hall"
    elif theater == 'playhouse':
        theaterName = 'Playhouse Theater'

    theaterObject = models.Theater.objects.filter(name=theaterName)

    # Create the variable in this scope for referencing later
    customer = models.Customer(firstName="temp", lastName="temp")

    # TODO: Add error handling for corrupted name
    # Check if a middle name was provided
    if len(nameParts) > 2:
        firstname = nameParts[0]
        middlename = nameParts[1]
        lastname = nameParts[2]

        # Use filter. If len = 1, then the user exists. If not, then create it.

        customers = models.Customer.objects.filter(firstName=firstname, middleName=middlename, lastName=lastname)

        # A record already exists for this customer.
        if len(customers) == 1:
            customer = customers[0]
        elif len(customers) == 0:
            customer = models.Customer(firstName=firstname, middleName=middlename, lastName=lastname)
            customer.save()

    else:
        firstname = nameParts[0]
        lastname = nameParts[1]

        customers = models.Customer.objects.filter(firstName=firstname, lastName=lastname)

        # A record already exists for this customer.
        if len(customers) == 1:
            customer = customers[0]
        elif len(customers) == 0:
            customer = models.Customer(firstName=firstname, lastName=lastname)
            customer.save()

    # We have the customer, now get the rest of the information we need for creating a ticket.
    # Format of seats is a string like: "A1,B3,A2"

    # Get a set of seats
    seatObjects = []
    rows = []
    sections = []

    individualSeatParts = seats.split(',')
    for i, part in enumerate(individualSeatParts):
        rows.append(models.Row.objects.get(name=part[0]))
        seatObjects.append(models.Seat.objects.get(number=int(part[1])))

        # Filter through the sections containing this row to find the one that is in the specified theater
        # Find the section that this row is in that is itself in the theater
        for section in rows[i].section_set.all():

            matchingTheaters = section.theater_set.filter(name=theaterName)

            if len(matchingTheaters) == 1:
                sections.append(section)
                break

    # Get the show
    performance = utility.getPerformanceOnDateAndTime(year, month, day, hour, minute)

    # For each seat, create a new ticket.
    for i, seat in enumerate(seatObjects):
        # First, do the logic for saving the single ticket


        ticket = models.Ticket.objects.create(paid=bool(paid))
        if bool(paid) == True:
            ticket.cash = bool(payment_method)
        ticket.datePurchased = datetime.datetime.now()
        ticket.door = bool(door_reservation)
        ticket.printed = bool(printed)
        ticket.customer.add(customer)
        ticket.seat.add(seat)
        ticket.row.add(rows[i])
        ticket.section.add(sections[i])
        ticket.season.add(models.Show.objects.get(name=show).season_set.all()[0])
        ticket.show.add(models.Show.objects.get(name=show))
        ticket.performance.add(performance)
        ticket.save()

    context = {}
    context['show'] = show
    context['theater'] = theater
    context['year'] = year
    context['month'] = month
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    context['seats'] = seats
    context['paid'] = paid
    context['name'] = name
    context['door_reservation'] = door_reservation
    context['printed'] = printed
    context['payment_method'] = payment_method
    test_str = show + theater + "---" + str(year) + "---" + str(month) + "---" + str(day) + "---" + str(
        hour) + "---" + str(minute) + "---" + seats + "---" + str(
        paid) + "---" + name + "---" + "---" + door_reservation + "---" + printed + "---" + payment_method
    return HttpResponse(test_str)

def buySeasonTicket(request):
    my_seasons = models.Season.objects.all
    my_theater = models.Theater.objects.all
    context = {
        'seasons': my_seasons,
        'theaters': my_theater
    }

    return render(request, 'webapp/buySeasonTicket.html', context)

def seasonSeatSelection(request, blank, theater, season, day, hour, minute):
    my_str =  theater + "--" + season + "--" +  day + "--" + str(hour) + "--" + str(minute)
    context = {}
    context['theater'] = theater
    context['season'] = season
    context['day'] = day
    context['hour'] = hour
    context['minute'] = minute
    return render(request, 'webapp/seasonSeatSelection.html', context)

def seatSelect(request):
    return render(request, 'webapp/seatSelection.html')

def seasonSeatSelect(request):
    return render(request, 'webapp/seasonSeatSelection.html')

def confirmation(request):
    return render(request, 'webapp/confirmation.html')

def help(request):
    return render(request, 'webapp/help.html')

def populatePlayhouseSeats():
    context = {}
    # Row R1A
    for i in range(1,2):
        key = 'R1A' + str(i)
        context[key] = 'available'
    # Row R2A
    for i in range(1,5):
        key = 'R2A' + str(i)
        context[key] = 'available'
    # Row R3A
    for i in range(1,5):
        key = 'R3A' + str(i)
        context[key] = 'available'
    # Row R4A
    for i in range(1,2):
        key = 'R4A' + str(i)
        context[key] = 'available'
    # Row L0A
    for i in range(1,4):
        key = 'L0A' + str(i)
        context[key] = 'available'
    # Row L1A
    for i in range(1,6):
        key = 'L1A' + str(i)
        context[key] = 'available'
    # Row L2A
    for i in range(1,10):
        key = 'L2A' + str(i)
        context[key] = 'available'
    # Row L3A
    for i in range(1,10):
        key = 'L3A' + str(i)
        context[key] = 'available'
    # Row L4A
    for i in range(1,7):
        key = 'L4A' + str(i)
        context[key] = 'available'
    # Row L5A
    for i in range(1,5):
        key = 'L5A' + str(i)
        context[key] = 'available'
    # Row R1B
    for i in range(1,3):
        key = 'R1B' + str(i)
        context[key] = 'available'
    # Row R2B
    for i in range(1,8):
        key = 'R2B' + str(i)
        context[key] = 'available'
    # Row R3B
    for i in range(1,8):
        key = 'R3B' + str(i)
        context[key] = 'available'
    # Row R4B
    for i in range(1,3):
        key = 'R4B' + str(i)
        context[key] = 'available'
    # Row R1C
    for i in range(1,4):
        key = 'R1C' + str(i)
        context[key] = 'available'
    # Row R2C
    for i in range(1,9):
        key = 'R2C' + str(i)
        context[key] = 'available'
    # Row R3C
    for i in range(1,9):
        key = 'R3C' + str(i)
        context[key] = 'available'
    # Row R4C
    for i in range(1,4):
        key = 'R4C' + str(i)
        context[key] = 'available'
    # Row R1D
    for i in range(1,4):
        key = 'R1D' + str(i)
        context[key] = 'available'
    # Row R2D
    for i in range(1,12):
        key = 'R2D' + str(i)
        context[key] = 'available'
    # Row R3D
    for i in range(1,12):
        key = 'R3D' + str(i)
        context[key] = 'available'
    # Row R4D
    for i in range(1,4):
        key = 'R4D' + str(i)
        context[key] = 'available'
    # Row R1E
    for i in range(1,5):
        key = 'R1E' + str(i)
        context[key] = 'available'
    # Row R2E
    for i in range(1,14):
        key = 'R2E' + str(i)
        context[key] = 'available'
    # Row R3E
    for i in range(1,14):
        key = 'R3E' + str(i)
        context[key] = 'available'
    # Row R4E
    for i in range(1,5):
        key = 'R4E' + str(i)
        context[key] = 'available'
    # Row R1F
    for i in range(1,6):
        key = 'R1F' + str(i)
        context[key] = 'available'
    # Row R2F
    for i in range(1,17):
        key = 'R2F' + str(i)
        context[key] = 'available'
    # Row R3F
    for i in range(1,17):
        key = 'R3F' + str(i)
        context[key] = 'available'
    # Row R4F
    for i in range(1,6):
        key = 'R4F' + str(i)
        context[key] = 'available'
    # Row R1G
    for i in range(1,6):
        key = 'R1G' + str(i)
        context[key] = 'available'
    # Row R2G
    for i in range(1,18):
        key = 'R2G' + str(i)
        context[key] = 'available'
    # Row R3G
    for i in range(1,18):
        key = 'R3G' + str(i)
        context[key] = 'available'
    # Row R4G
    for i in range(1,6):
        key = 'R4G' + str(i)
        context[key] = 'available'
    # Row L1B
    for i in range(1,5):
        key = 'L1B' + str(i)
        context[key] = 'available'
    # Row L2B
    for i in range(1,12):
        key = 'L2B' + str(i)
        context[key] = 'available'
    # Row L3B
    for i in range(1,12):
        key = 'L3B' + str(i)
        context[key] = 'available'
    # Row L4B
    for i in range(1,6):
        key = 'L4B' + str(i)
        context[key] = 'available'
    # Row L1C
    for i in range(1,4):
        key = 'L1C' + str(i)
        context[key] = 'available'
    # Row L2C
    for i in range(1,14):
        key = 'L2C' + str(i)
        context[key] = 'available'
    # Row L3B
    for i in range(1,14):
        key = 'L3C' + str(i)
        context[key] = 'available'
    # Row L4C
    for i in range(1,6):
        key = 'L4C' + str(i)
        context[key] = 'available'
    return context

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
    # Row S1A
    for i in range(1,9):
        key = 'S1A' + str(i)
        context[key] = 'available'
    # Row S2A
    for i in range(1,14):
        key = 'S2A' + str(i)
        context[key] = 'available'
    # Row S3A
    for i in range(1,15):
        key = 'S3A' + str(i)
        context[key] = 'available'
    # Row S4A
    for i in range(1,14):
        key = 'S4A' + str(i)
        context[key] = 'available'
    # Row S5A
    for i in range(1,9):
        key = 'S5A' + str(i)
        context[key] = 'available'
    # Row S1B
    for i in range(1,9):
        key = 'S1B' + str(i)
        context[key] = 'available'
    # Row S2B
    for i in range(1,14):
        key = 'S2B' + str(i)
        context[key] = 'available'
    # Row S3B
    for i in range(1,15):
        key = 'S3B' + str(i)
        context[key] = 'available'
    # Row S4B
    for i in range(1,14):
        key = 'S4B' + str(i)
        context[key] = 'available'
    # Row S5B
    for i in range(1,9):
        key = 'S5B' + str(i)
        context[key] = 'available'
    # Row S1C
    for i in range(1,9):
        key = 'S1C' + str(i)
        context[key] = 'available'
    # Row S2C
    for i in range(1,14):
        key = 'S2C' + str(i)
        context[key] = 'available'
    # Row S3C
    for i in range(1,15):
        key = 'S3C' + str(i)
        context[key] = 'available'
    # Row S4C
    for i in range(1,14):
        key = 'S4C' + str(i)
        context[key] = 'available'
    # Row S5C
    for i in range(1,9):
        key = 'S5C' + str(i)
        context[key] = 'available'
    # Row S1D
    for i in range(1,9):
        key = 'S1D' + str(i)
        context[key] = 'available'
    # Row S2D
    for i in range(1,14):
        key = 'S2D' + str(i)
        context[key] = 'available'
    # Row S3D
    for i in range(1,15):
        key = 'S3D' + str(i)
        context[key] = 'available'
    # Row S4D
    for i in range(1,14):
        key = 'S4D' + str(i)
        context[key] = 'available'
    # Row S5D
    for i in range(1,9):
        key = 'S5D' + str(i)
        context[key] = 'available'
    # Row S1E
    for i in range(1,9):
        key = 'S1E' + str(i)
        context[key] = 'available'
    # Row S2E
    for i in range(1,14):
        key = 'S2E' + str(i)
        context[key] = 'available'
    # Row S3E
    for i in range(1,15):
        key = 'S3E' + str(i)
        context[key] = 'available'
    # Row S4E
    for i in range(1,14):
        key = 'S4E' + str(i)
        context[key] = 'available'
    # Row S5E
    for i in range(1,9):
        key = 'S5E' + str(i)
        context[key] = 'available'
    # Row S1F
    for i in range(1,9):
        key = 'S1F' + str(i)
        context[key] = 'available'
    # Row S2F
    for i in range(1,13):
        key = 'S2F' + str(i)
        context[key] = 'available'
    # Row S3F
    for i in range(1,15):
        key = 'S3F' + str(i)
        context[key] = 'available'
    # Row S4F
    for i in range(1,13):
        key = 'S4F' + str(i)
        context[key] = 'available'
    # Row S5F
    for i in range(1,9):
        key = 'S5F' + str(i)
        context[key] = 'available'
    # Row S1G
    for i in range(1,9):
        key = 'S1G' + str(i)
        context[key] = 'available'
    # Row S2G
    for i in range(1,13):
        key = 'S2G' + str(i)
        context[key] = 'available'
    # Row S3G
    for i in range(1,15):
        key = 'S3G' + str(i)
        context[key] = 'available'
    # Row S4G
    for i in range(1,13):
        key = 'S4G' + str(i)
        context[key] = 'available'
    # Row S5G
    for i in range(1,9):
        key = 'S5G' + str(i)
        context[key] = 'available'
    # Row S1H
    for i in range(1,9):
        key = 'S1H' + str(i)
        context[key] = 'available'
    # Row S2H
    for i in range(1,13):
        key = 'S2H' + str(i)
        context[key] = 'available'
    # Row S3H
    for i in range(1,15):
        key = 'S3H' + str(i)
        context[key] = 'available'
    # Row S4H
    for i in range(1,10):
        key = 'S4H' + str(i)
        context[key] = 'available'
    # Row S5H
    for i in range(1,9):
        key = 'S5H' + str(i)
        context[key] = 'available'
    # Row S1I
    for i in range(1,9):
        key = 'S1I' + str(i)
        context[key] = 'available'
    # Row S2I
    for i in range(1,13):
        key = 'S2I' + str(i)
        context[key] = 'available'
    # Row S3I
    for i in range(1,15):
        key = 'S3I' + str(i)
        context[key] = 'available'
    # Row S4I
    for i in range(1,10):
        key = 'S4I' + str(i)
        context[key] = 'available'
    # Row S5I
    for i in range(1,9):
        key = 'S5I' + str(i)
        context[key] = 'available'
    # Row S1J
    for i in range(1,8):
        key = 'S1J' + str(i)
        context[key] = 'available'
    # Row S2J
    for i in range(1,13):
        key = 'S2J' + str(i)
        context[key] = 'available'
    # Row S3J
    for i in range(1,15):
        key = 'S3J' + str(i)
        context[key] = 'available'
    # Row S4J
    for i in range(1,10):
        key = 'S4J' + str(i)
        context[key] = 'available'
    # Row S5J
    for i in range(1,8):
        key = 'S5J' + str(i)
        context[key] = 'available'
    # Row S1K
    for i in range(1,8):
        key = 'S1K' + str(i)
        context[key] = 'available'
    # Row S2K
    for i in range(1,13):
        key = 'S2K' + str(i)
        context[key] = 'available'
    # Row S3K
    for i in range(1,15):
        key = 'S3K' + str(i)
        context[key] = 'available'
    # Row S4K
    for i in range(1,10):
        key = 'S4K' + str(i)
        context[key] = 'available'
    # Row S5K
    for i in range(1,8):
        key = 'S5K' + str(i)
        context[key] = 'available'
    # Row S1L
    for i in range(1,8):
        key = 'S1L' + str(i)
        context[key] = 'available'
    # Row S2L
    for i in range(1,13):
        key = 'S2L' + str(i)
        context[key] = 'available'
    # Row S3L
    for i in range(1,21):
        key = 'S3L' + str(i)
        context[key] = 'available'
    # Row S4L
    for i in range(1,10):
        key = 'S4L' + str(i)
        context[key] = 'available'
    # Row S5L
    for i in range(1,8):
        key = 'S5L' + str(i)
        context[key] = 'available'
    return context
