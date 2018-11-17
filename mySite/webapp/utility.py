from . import models
import datetime


"""Returns a list of performances in a specific season"""
def getPerformancesInSeason(season):
    shows = models.Season.objects.get(name=season).shows.all()

    performances = []

    # Iterate through every show in the Season
    for show in shows:

        # iterate through all performances in a specific show
        for performance in show.performances.all():

            performances.append(performance)

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