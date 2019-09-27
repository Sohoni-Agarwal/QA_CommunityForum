from django.shortcuts import render
from django.views.generic import TemplateView


# def index(request):
#  return render(request, 'frontend/templates/index.html')


class HomePageView(TemplateView):
    template_name = 'login.html'
