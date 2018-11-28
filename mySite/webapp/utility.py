from . import models
import datetime

#TODO: Create a function that gets the Section (in a specified Theater) that contains a specified row and seat


#TODO: Clean up
def getPerformancesByLocationAndDate(season, theater, year, month, day):
    showDetails = []

    # Create a datetime.date object for the day of the year
    date = datetime.date(year, month, day)

    # Get the set of shows
    shows = models.Show.objects.all()

    # Filter for shows that have performances that are on the specified day
    for show in shows:

        # build a list of performances that are for this show and on this day
        performances = []

        # A sentinal value for keeping track of whether this show has a showtime on the selected day
        relevant = False

        # Iterate through the performances in this show
        for performance in show.performances.all():

            # Check if the current performance is on the right day of the year
            if performance.time.date() == date:
                relevant = True

                # If it is, then add it to the list
                performances.append(performance)

        # We now have list of the relevant performances

        # Ensure that we only reply with details of this show if it is relevant
        if relevant == True:

            # Build a string with all of their showtimes.
            showtimes = ""

            for performance in performances:
                showtimes += str(performance.time)

            # showtimes is only the showtimes that are on this day

            # Build a response dictionary to send back
            dict = {'name': str(show.name),
                    'img': str(show.img),
                    'runtime': str(show.runtime),
                    'genre': str(show.genre),
                    'summary': str(show.summary),
                    'season': season,
                    'showtimes': showtimes,
                    'theater': theater,
                    'day': month + "/" + day + "/" + year
                    }

            # Add this response dictionary to the list of responses
            showDetails.append(dict)

    # Build the context
    context = {
        'theaters': list(models.Theater.objects.all()),
        'performances': showDetails
    }

def getSortedPerformancesInShow(show):

    show = models.Show.objects.get(name=show)

    times = []

    for performance in show.performances.all():

        times.append(performance.time)

    times.sort()

    print("MAGIC:")

    print(times)

    return times

"""Returns a list of performances in a specific season"""
def getPerformancesInSeason(season):
    shows = models.Season.objects.get(name=season).shows.all()

    performances = []

    # Iterate through every show in the Season
    for show in shows:

        # iterate through all performances in a specific show
        for performance in show.performances.all():

            if performance not in performances:

                performances.append(performance)

    return performances

"""Returns a list of performances that are on a particular date"""
def getPerformancesOnDate(year, month, day):
    # build a datetime object to use for comparison
    date_for_comparison = datetime.date(int(year), int(month), int(day))

    # create a list to hold results
    performances_on_date = []

    # Get the set of all Performances in the database
    performances = models.Performance.objects.all()

    # Iterate through every performance
    for performance in performances:
        # Compare the current performance's date to our criteria
        if performance.time.date() == date_for_comparison:
            # If their dates match, add it to the list of results
            performances_on_date.append(performance)

    return performances_on_date

"""Returns a list of performances that are on a particular date and at a particular time"""
def getPerformanceOnDateAndTime(year, month, day, hour, minute, theater):
    # build a datetime object to use for comparison
    date_for_comparison = datetime.date(int(year), int(month), int(day))

    # create a list to hold results
    performances_on_date = []

    # Get the set of all Performances in the database
    performances = models.Performance.objects.all()

    # Iterate through every performance
    for performance in performances:


        # Compare the current performance's date to our criteria
        if performance.time.date() == date_for_comparison and performance.time.hour == hour and performance.time.minute == minute and performance.theater.all()[0].name == theater:
            # If their dates match, add it to the list of results
            return performance




"""Returns a list of performances that are on a particular day of the week."""
def getPerformancesOnWeekday(day):
    # Build a dictionary of reference values.
    # These correspond to the values returned by Python's datetime.weekday() method
    weekdays = {'monday': 0,
                'teusday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday': 6}

    # Get the appropriate integer for the day we want, using the lowercase represetnation of the value
    weekday = weekdays[day.lower()]

    # Build a list to keep our results in
    performances_on_wednesday = []

    # Get the set of all performances in the database
    performances = models.Performance.objects.all()

    # Iterate through each performance
    for performance in performances:
        # Check if its weekday matches our criteria
        if performance.time.weekday() == weekday:
            # If it does, add it to the list of results
            performances_on_wednesday.append(performance)

    return performances_on_wednesday

"""Returns a list of performances that are on a particular day of the week."""
def getPerformancesOnWeekdayInSeason(day, season):
    # Build a dictionary of reference values.
    # These correspond to the values returned by Python's datetime.weekday() method
    weekdays = {'monday': 0,
                'teusday': 1,
                'wednesday': 2,
                'thursday': 3,
                'friday': 4,
                'saturday': 5,
                'sunday': 6}

    # Get the appropriate integer for the day we want, using the lowercase represetnation of the value
    weekday = weekdays[day.lower()]

    # Build a list to keep our results in
    performances_on_weekday = []

    # Get the set of all performances in the database
    performances = getPerformancesInSeason(season)

    # Iterate through each performance
    for performance in performances:

        # Check if its weekday matches our criteria
        if performance.time.weekday() == weekday:

            # If it does, add it to the list of results
            performances_on_weekday.append(performance)

    return performances_on_weekday


"""Check and see if a ticket exists for a particular theater, date, time, and seat."""
def doesTicketExist(theater, section, row, seat, year, month, day, hour, minute):
    #Create a datetime object to use for comparison
    date = datetime.date(int(year), int(month), int(day))

    #Get the theater with the specified name
    theaterObject = models.Theater.objects.get(name=theater)

    try:

        #Iterate through every Performance in that theater
        for performance in theaterObject.performance_set.all():

            #Check for one that matches the specified date and time
            if performance.time.date() == date and performance.time.hour == hour and performance.time.minute == minute:

                #Get the set of tickets that refer to this performance
                tickets = performance.ticket_set.all()

                #Iterate through the tickets for this performance
                for ticket in tickets:

                    #Check for a ticket that matches the seat, section, and row specified
                    if str(ticket.section.all()[0]).lower() == section.lower() and str(ticket.seat.all()[0]).lower() == str(seat).lower() and str(ticket.row.all()[0]).lower() == row.lower():

                        #If a ticket is found, return true
                        return True

    #Catch the exception in the edge case that the Ticket has an empty Section, Seat, or Row
    except IndexError:

        return False

    #Return false if no ticket is found
    return False