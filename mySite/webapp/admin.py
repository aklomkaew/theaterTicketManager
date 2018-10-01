from django.contrib import admin

# Register your models here.
import webapp.models

admin.site.register(webapp.models.Season)
admin.site.register(webapp.models.Show)
admin.site.register(webapp.models.Performance)
admin.site.register(webapp.models.Theater)
admin.site.register(webapp.models.Section)
admin.site.register(webapp.models.Row)
admin.site.register(webapp.models.Seat)
admin.site.register(webapp.models.Ticket)
admin.site.register(webapp.models.Customer)
admin.site.register(webapp.models.PriceGroup)
admin.site.register(webapp.models.SeasonTicketHolder)