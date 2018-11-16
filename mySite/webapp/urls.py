from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('performance/', views.performance, name='performance'),
    path('contact/', views.contact, name='contact'),
    path('buySeasonTickets/', views.buySeasonTicket, name='buySeasonTickets'),
    path('admin/', views.admin, name='admin'),
    path('payment/', views.payment, name='payment'),
    path('seatSelection/<str:theater>/<str:show>/<str:date>/<str:time>/', views.seatSelection, name='seatSelection'),
    path('seasonSeatSelection/<str:theater>/<str:season>/<str:day>/<str:time>/', views.seasonSeatSelection, name='seasonSeatSelection'),
    path('seatSelection/concertHall/', views.concertHall, name='concertHall'),
    path('confirmationPage/<str:seat_numbers>/', views.confirmationPage, name='confirmationPage'),
    path('seatSelection/', views.seatSelect, name='seatSelection')
]
