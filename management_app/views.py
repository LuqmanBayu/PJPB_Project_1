from django.contrib.auth import _get_backends, _get_user_session_key, HASH_SESSION_KEY, SESSION_KEY, \
    BACKEND_SESSION_KEY, user_logged_in, login
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import rotate_token
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def SecondPage(request):
    return render(request,"first_page.html")

def Loginpage(request):
    return render(request,"login_page.html")

