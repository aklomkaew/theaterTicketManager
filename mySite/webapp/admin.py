from django.contrib import admin

#Guide for modifying the displays for each model: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

# Register your models here.
from webapp.models import *


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_shows')

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'runtime', 'summary', 'img', 'get_performances', 'get_season')

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('time', 'get_theater', 'get_show')

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'get_sections')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_rows', 'get_pricegroups')

@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_seats', 'get_section')


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('number', 'get_row')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name', 'get_seat', 'get_section', 'get_row', 'get_performance', 'get_show', 'get_season', 'paid', 'datePurchased', 'door', 'printed')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'middleName', 'lastName', 'address', 'email', 'phone', 'get_tickets')

@admin.register(PriceGroup)
class PriceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_sections')

@admin.register(SeasonTicketHolder)
class SeasonTicketHolderAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name', 'get_customer_address', 'valid', 'get_seasons')

admin.site.site_header = "Theater Ticket Manager"
admin.site.site_title = "Theater Ticket Manager"