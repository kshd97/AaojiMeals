from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, Http404,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from .models import *

from django.core.mail import send_mail
# import smtplib
# from email.mime.text import MIMEText

# Create your views here.

def index(request):
	return render(request,'info/index.djt',None)