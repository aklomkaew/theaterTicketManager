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
    path('payment/<str:theater>/<str:performance>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<str:seats>/', views.payment, name='payment'),
    path('seasonPayment/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/<str:seats>/', views.seasonPayment, name='seasonPayment'),

    path('seatSelection/<str:performance>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/', views.seatSelection, name='seatSelection'),
    path('seatSelection/<str:performance>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/concertHall/', views.concertHall, name='concertHall'),
    path('seasonSeatSelection/<str:blank>/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/', views.seasonSeatSelection, name='seasonSeatSelection'),
    path('seasonSeatSelection/<str:blank>/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/concertHall/', views.seasonConcertHall, name='seasonConcertHall'),
    path('seasonConfirmationPage/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/<str:seats>/<str:paid>/<str:name>/<str:phoneNumber>/<str:email>/<str:door_reservation>/<str:printed>/<str:payment_method>/', views.season_confirmationPage, name='seasonConfirmationPage'),
    path('confirmationPage/<str:performance>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<str:seats>/<str:paid>/<str:name>/<str:door_reservation>/<str:printed>/<str:payment_method>/', views.confirmationPage, name='confirmationPage')
    path('confirmation/', views.confirmation, name='confirmation'),
    path('help/', views.help, name='help'),
]
