from webapp.models import Ticket
from django.forms.models import ModelForm

class TicketsForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'seat', 'show', 'season', 'performance', 'date', 'paid', 'door']
