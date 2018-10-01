from django.db import models

# Create your models here.

#TODO: Change these to references to customers, shows, etc.?
#TODO: Change the reference system to use the ForeignKey Relationship. Maybe?
#Figure out how references work in Django
class Season(models.Model):
    #id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    #Insert a one-to-many referance to a list of Shows.

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=50)
    #Insert a one-to-many reference to a list of Performances.
    #Insert a one-to-one reference to the Season this Show is in.

    def __str__(self):
        return self.name


class Performance(models.Model):
    date = models.DateTimeField()#Date and time of the performance.
    #Insert a one-to-one reference to the Show this Performance is for.
    #Insert a one-to-one reference to the Theater that this Performance is being shown in. Seats are referenced indirectly this way.


#The site that a Performance is held in. Contains the seating information, name, and location.
class Theater(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)#Location of the theater
    #TODO: Figure out how to arrange seating.

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=50)
    basePrice = models.DecimalField(max_digits=6, decimal_places=2)#Representing the unmodified price of this section.
    #insert a one-to-one reference to a Theater, representing what Theater this section is in.
    #insert a one-to-many reference to a list of Rows

    def __str__(self):
        return self.name


class Row(models.Model):
    name = models.CharField(max_length=10)#Number or name of the row.
    #one-to-many reference to a set of Seats
    #One-to-one reference to the Section that contains this Row.

    def __str__(self):
        return self.name


class Seat(models.Model):
    number = models.IntegerField()#Number of the seat
    #One-to-one reference to the row that contains this Seat


class Ticket(models.Model):
    name = models.CharField(max_length=50)#Name of the customer who purchased the ticket. Change this to Customer reference?
    seat = models.CharField(max_length=10)
    season = models.CharField(max_length=50)
    show = models.CharField(max_length=100)#Name of the show that this ticket is valid for
    performance = models.DateTimeField()#The individual performance.
    paid = models.BooleanField(default=False)#Whether or not the ticket has been paid. Keeps track of advance tickets.
    date = models.DateTimeField()#Date of the performance that the ticket is valid for
    datePurchased = models.DateTimeField()#When the ticket was purchased.
    door = models.BooleanField()#Whether or not the ticket was purchased at the door
    printed = models.BooleanField()#Whether or not the ticket has been printed.

    def __str__(self):
        return self.name


class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=400)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return str(self.firstName) + " " + str(self.middleName) + " " + str(self.lastName)


class PriceGroup(models.Model):
    name = models.CharField(max_length=100)#Name used to select describe the group (i.e. First Bank, comp, volunteers, etc.)
    price = models.DecimalField(max_digits=6, decimal_places=2)#Price for this group. #TODO: How to handle on a per-section basis.

    def __str__(self):
        return self.name


class SeasonTicketHolder(models.Model):
    custRef = models.CharField(max_length=20)#A reference to the customer who owns the season tickets.
    #tickets = models.ForeignKey()#A list of references to tickets in the Tickets table.
    #TODO: Not sure how these work exactly, but you can make a One-To_Many Foreign Key Relationship to refer to items in another model.
