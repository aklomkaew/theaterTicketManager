from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('theater/', views.theater, name='theater'),
    path('performance/', views.performance, name='performance'),
]
