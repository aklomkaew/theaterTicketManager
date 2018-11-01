from django.db import models
# from django.contrib.auth.models import User
#
# class Post(models.Model):
#     post = models.CharField(max_length=500)
#     user = models.ForeignKey(User)


# import webapp.models
#
# ticket = Ticket()
# ticket.firstname = "john"
# ticket.date = ""
# ticket.Save()
#
# ticket = Ticket.filter(name="john")

class Seat(models.Model):
    number = models.IntegerField()#Number of the seat

    def __str__(self):
        return str(self.number)

    #row = models.ForeignKey(Row, on_delete=models.CASCADE, null=True) #One-to-one reference to the row that contains this Seat

class Row(models.Model):
    name = models.CharField(max_length=10)#Number or name of the row.
    seats = models.ManyToManyField(Seat)
    #one-to-many reference to a set of Seats
    #One-to-one reference to the Section that contains this Row.

    def __str__(self):
        return self.name

class PriceGroup(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=50)
    rows = models.ManyToManyField(Row)
    pricegroups = models.ManyToManyField(PriceGroup)
    #theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True)
    #insert a one-to-one reference to a Theater, representing what Theater this section is in.
    #insert a one-to-many reference to a list of Rows

    def __str__(self):
        return self.name

    def getName(self):
        return self.name


#The site that a Performance is held in. Contains the seating information, name, and location.
class Theater(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)#Location of the theater
    sections = models.ManyToManyField(Section)

    def __str__(self):
        return self.name


class Performance(models.Model):
    time = models.DateTimeField()#Date and time of the performance.
    theater = models.OneToOneField(Theater, on_delete=models.CASCADE)
    #show = models.OneToOneField(Show, on_delete=models.CASCADE)

    #TODO: Combine the name of the show with the date of this performance
    #def __str__(self):
        #return self.name



class Show(models.Model):
    name = models.CharField(max_length=50)
    performances = models.ManyToManyField(Performance)
    #Insert a one-to-many reference to a list of Performances.
    #Insert a one-to-one reference to the Season this Show is in.


    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=50)
    shows = models.ManyToManyField(Show)
    #Insert a one-to-many referance to a list of Shows.

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


class Ticket(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)#Name of the customer who purchased the ticket. Change this to Customer reference?
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    season = models.OneToOneField(Season, on_delete=models.CASCADE)
    show = models.OneToOneField(Show, on_delete=models.CASCADE)#Name of the show that this ticket is valid for
    performance = models.OneToOneField(Performance, on_delete=models.CASCADE)#The individual performance.
    paid = models.BooleanField(default=False)#Whether or not the ticket has been paid. Keeps track of advance tickets.
    date = models.DateTimeField()#Date of the performance that the ticket is valid for
    datePurchased = models.DateTimeField()#When the ticket was purchased.
    door = models.BooleanField()#Whether or not the ticket was purchased at the door
    printed = models.BooleanField(default=False)#Whether or not the ticket has been printed.

    def __str__(self):
        return self.name
