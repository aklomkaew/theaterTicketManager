from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('performance/', views.performance, name='performance'),
    path('getPerformances/', views.getPerformances, name='getPerformances'),
    path('getPerformances/<str:theater>/<str:month>/<str:day>/<str:year>', views.getPerformances, name='getPerformancesARGS'),
    path('contact/', views.contact, name='contact'),
    path('buySeasonTickets/', views.buySeasonTicket, name='buySeasonTickets'),
    path('admin/', views.admin, name='admin'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('help/', views.help, name='help'),
    path('payment/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<str:seats>/', views.payment, name='payment'),
    path('seatSelection/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/', views.seatSelection, name='seatSelection'),
    path('seatSelection/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/concertHall/', views.concertHall, name='concertHall'),
    path('seatSelection/<str:season>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/', views.seasonSeatSelection, name='seasonSeatSelection'),
    path('confirmationPage/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<str:seats>/<str:paid>/<str:name>/<str:door_reservation>/<str:printed>/<str:payment_method>/', views.confirmationPage, name='confirmationPage')
]
