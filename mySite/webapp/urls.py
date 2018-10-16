from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('performance/', views.performance, name='performance'),
    path('contact/', views.contact, name='contact'),
    path('buySeasonTickets/', views.buySeasonTicket, name='buySeasonTickets'),
    path('payment/', views.payment, name='payment'),
]
