from django.urls import path
from . import views

urlpatterns = [
     path('', views.register, name='register'),
    # path('', views.HomePageView.as_view(), name='home')
]