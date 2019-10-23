from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# def index(request):
#  return render(request, 'frontend/templates/home.html')


# class HomePageView(TemplateView):
def login(request):
    if request.method == 'GET':
        context = ''
        return render(request, './login.html', {'context': context})

    elif request.method == 'POST':
        e_mail = request.POST.get('e_mail', '')
        password = request.POST.get('password', '')

        user = authenticate(request, email=e_mail, password=password)
        if user is not None:
            login(request, user)
            return redirect('./home.html')
            # return HttpResponseRedirect('/')
        else:
            context = {'error': 'Wrong credentials'}  # to display error?
            return render(request, './login.html', {'context': context})


'''def login_request(request):
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})'''
