from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('performance/', views.performance, name='performance'),
    path('getPerformances/', views.getPerformances, name='getPerformances'),
    path('getPerformances/<str:theater>/<str:month>/<str:day>/<str:year>', views.getPerformances, name='getPerformancesARGS'),
    path('getShowtimes/<str:showName>/', views.getShowtimes, name='getShowtimes'),
    path('contact/', views.contact, name='contact'),
    path('buySeasonTickets/', views.buySeasonTicket, name='buySeasonTickets'),
    path('admin/', views.admin, name='admin'),
    path('payment/<str:show>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<str:seats>/', views.payment, name='payment'),
    path('seasonPayment/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/<str:seats>/', views.seasonPayment, name='seasonPayment'),
    path('seatSelection/<str:show>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/', views.seatSelection, name='seatSelection'),
    path('seatSelection/<str:show>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/concertHall/', views.concertHall, name='concertHall'),
    path('seatSelection/<str:show>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/playhouse/', views.playhouse, name='playhouse'),
    path('seasonSeatSelection/<str:blank>/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/', views.seasonSeatSelection, name='seasonSeatSelection'),
    path('seasonSeatSelection/<str:blank>/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/concertHall/', views.seasonConcertHall, name='seasonConcertHall'),
    path('seasonSeatSelection/<str:blank>/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/playhouse/', views.seasonPlayhouse, name='seasonPlayhouse'),
    path('seasonConfirmationPage/<str:theater>/<str:season>/<str:day>/<int:hour>/<int:minute>/<str:seats>/<int:paid>/<str:name>/<str:address>/<str:phoneNumber>/<str:email>/<str:door_reservation>/<str:printed>/<str:payment_method>/<str:total>/<str:seats_prices>/', views.season_confirmationPage, name='seasonConfirmationPage'),
    path('confirmationPage/<str:show>/<str:theater>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<str:seats>/<int:paid>/<str:name>/<str:door_reservation>/<str:printed>/<str:payment_method>/<str:total>/<str:seats_prices>/', views.confirmationPage, name='confirmationPage'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('help/', views.help, name='help'),
    path('authFail/', views.authFail, name='authFail')
]
