from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import CustomUserRegisterForm
from .tokens import account_activation_token


def register(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = CustomUserRegisterForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

'''
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from users.forms import CustomUserRegisterForm, CustomUserLoginForm, CustomUserChangeDetailsForm


# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView


@login_required
@transaction.atomic
def update_user_details(request):
    if request.method == 'POST':
        user_register_form = CustomUserRegisterForm(request.POST, instance=request.UserMasterTable)
        user_login_form = CustomUserLoginForm(request.POST, instance=request.UserMasterTable)
        user_details_form = CustomUserChangeDetailsForm(request.POST, instance=request.user.UserMasterTable)

        if user_register_form.is_valid() and user_details_form.is_valid():
            user_register_form.save()
            user_login_form.login()
            user_details_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_register_form = CustomUserRegisterForm(instance=request.user)
        user_login_form = CustomUserLoginForm(instance=request.user.login)
        user_details_form = CustomUserChangeDetailsForm(instance=request.user.UserMasterTable)
    return render(request, 'templates/account_settings.html', {
        'user_register_form': user_register_form,
        'user_details_form': user_details_form,
        'user_login_form': user_login_form
    })

'''