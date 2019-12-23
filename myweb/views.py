from django.shortcuts import render
from .models import Register																																																											
from django.http import HttpResponse
from .form import RegisterForm
from . import apihandler
import os
import tweepy

def new_index(request):
	return render(request,'test.html',{'text':'hello World'})

def apicall(request):
	response = apihandler.apirequest()
	return render(request,'apihandler.html',{'response':response})

def users(request):
	users = Register.objects.all()
	if request.method == 'GET':
		return render(request,'users.html',{'users':users})
	else:
		return HttpResponse("<h1>Post Request is not allowed to this page</h1>")																							

def register(request):
	form = RegisterForm()

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return new_index(request)
		else:
			print('Invalid form')			

	return render(request,'Registration.html',{'form':form})

def index(request):
	return render(request,'index.html',{})

def filters(request):
	return render(request,'filters.html')


