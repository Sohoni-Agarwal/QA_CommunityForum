from django.views.generic import TemplateView


# def index(request):
#  return render(request, 'frontend/templates/home.html')


class HomePageView(TemplateView):
    template_name = 'login.html'


