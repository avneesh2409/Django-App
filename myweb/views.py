from django.shortcuts import render
from .form import *
import pickle
import sklearn
import os
import tweepy
from .twitter_mining import get_tweets
# Create your views here.

def new_index(request):
	return render(request,'test.html',{'text':'hello World'})

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

def twitter_mining(request):
	# search=None
	# if request.method == 'POST':
	# 	form = twitter_Mining(request.POST)
	# 	if form.is_valid():
	# 		search = form.cleaned_data.get('Search_element')
	# else :
	# 	form = twitter_Mining()
	return render(request,'twitter_mining.html')

def project(request):
	x=None
	y=None
	if request.method=='POST':
		form = NameForm(request.POST)
		if form.is_valid() :
			ApplicantIncome=	form.cleaned_data.get('ApplicantIncome')
			CoapplicantIncome=	form.cleaned_data.get('CoapplicantIncome')
			Gender=			form.cleaned_data.get('Gender')
			LoanAmont=		form.cleaned_data.get('LoanAmont')
			Loan_Amount_Term=	form.cleaned_data.get('Loan_Amount_Term')
			Credit_History=form.cleaned_data.get('Credit_History')
			Education=form.cleaned_data.get('Education')
			Married=form.cleaned_data.get('Married')
			Self_Employed=form.cleaned_data.get('Self_Employed')
			Dependents=form.cleaned_data.get('Dependents')
			Dependents1=form.cleaned_data.get('Dependents1')
			pwd = os.path.dirname(__file__)
			with open(pwd+'/check1.pkl', 'rb') as f:
				x = pickle.load(f)
			y_pred = x.predict([[float(ApplicantIncome), float(CoapplicantIncome), float(Loan_Amount_Term), float(LoanAmont),float(Gender),float(Credit_History),float(Education), float(Married), float(Self_Employed), float(Dependents),float(Dependents1)]])
			y=y_pred[0]
	else :
		form = NameForm()
	return render(request,'project.html',{'form':form,'y_pred':y})

