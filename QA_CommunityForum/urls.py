"""QA_CommunityForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from templates import views

from QA_CommunityForum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', views.HomePageView.as_view(), name='home'),
    # path('', views.TemplateView.as_view(template_name='login.html'), name='login'),

    # path('templates/views.py', views.login, name='login'),
    path('templates', include('templates.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),

    path('reset/password_reset', auth_views.PasswordResetView.as_view(),
         {'template_name': "templates/registration/password_reset_form.html"},
         name='password_reset'),
    path('reset/password_reset/done', auth_views.PasswordResetDoneView.as_view(),
         {'template_name': "templates/registration/password_reset_done.html"},
         name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
         auth_views.PasswordResetConfirmView.as_view(),
         {'template_name': "templates/registration/password_reset_confirm.html"},
         name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(),
         {'template_name': "templates/registration/password_reset_complete.html"},
         name='password_reset_complete'),
]
