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
    path('payment/', views.payment, name='payment'),
    path('seatSelection/', views.seatSelection, name='seatSelection'),
    path('seatSelection/<str:theater>/<str:day>/<str:time>/', views.seatSelection, name='seatSelectionARGS'),
    path('seasonSeatSelection/<str:season>/<str:theater>/<str:day>/<str:time>/', views.seasonSeatSelection, name='seasonSeatSelection'),
    path('concertHall/', views.concertHall, name='concertHall'),
    path('confirmationPage/<str:seat_numbers>/', views.confirmationPage, name='confirmationPage')
]
