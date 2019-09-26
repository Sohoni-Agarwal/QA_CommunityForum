from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index),
    path('', views.HomePageView.as_view(), name='home')
]
