from django.urls import path
from templates import views

urlpatterns = [

    path('', views.login, name='login'),
    path('login', views.register, name='register'),
    path('', views.home, name='home'),
    # path('', views.fpw, name='fpw'),
    # path('', views.pass_reset_complete, name='pass_reset_complete'),
    # path('', views.pass_reset_confirm, name='pass_reset_confirm'),
    # path('', views.pass_reset_done, name='pass_reset_done'),
    # path('', views.pass_reset_email, name='pass_reset_email'),

    path('base_header', views.answers, name='answers'),
    path('home', views.answers, name='answers'),
    path('', views.account_settings, name='account_settings'),
    path('', views.profile, name='profile'),
    path('', views.settings, name='settings'),
    # path('', views.HomePageView.as_view(), name='home')
]
