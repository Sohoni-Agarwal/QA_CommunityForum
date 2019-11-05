import email
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "login.html"


def register(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def fpw(request):
    return render(request, 'registration/password_reset_form.html')


def home(request):
    return render(request, 'home.html')


def answers(request):
    return render(request, 'answers.html')


def account_settings(request):
    return render(request, 'account_settings.html')


def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'settings.html')


def login(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'login.html', {'context': context})

    elif request.method == 'POST':
        e_mail = request.POST.get('e_mail', '')
        password = request.POST.get('password', '')

        user = authenticate(request, email=e_mail, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # return HttpResponseRedirect('/')
        else:
            context = {'error': 'Wrong credentials'}  # to display error?
            return render(request, 'login.html', {'context': context})
