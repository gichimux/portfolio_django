from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
	form = ContactForm()
	# request.method == 'POST'
	# name = request.POST.get('contact_name')
	# email = request.POST.get('contact_email')
	# content = request.POST.get('content')

	# if name and email and content:
	# 	try:
	# 		send_mail(name, content, email, ['dev.py.js@gmail.com'])
	# 	except BadHeaderError:
	# 		return HttpResponse('Invalid header found.') 
	# 	return HttpResponse('Email sent successfully')

	# else:
	return render(request, 'index.html', {'form': form})

def projects(request):
	return render(request, 'projects.html', {})

