from django.contrib import admin

# Register your models here.
from webapp.models import *

admin.site.register(Season)
admin.site.register(Show)
admin.site.register(Performance)
admin.site.register(Theater)
admin.site.register(Section)
admin.site.register(Row)
admin.site.register(Seat)
admin.site.register(Ticket)
admin.site.register(Customer)
admin.site.register(PriceGroup)

admin.site.site_header = "Theater Ticket Manager"
admin.site.site_title = "Theater Ticket Manager"