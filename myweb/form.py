from django import forms
from django.core import validators
from .models import Register,UserProfile

class NameForm(forms.Form):
    ApplicantIncome = forms.CharField(max_length=100)
    CoapplicantIncome = forms.CharField(max_length=100)
    Gender = forms.CharField(max_length=100)
    LoanAmont = forms.CharField(max_length=100)
    Loan_Amount_Term = forms.CharField(max_length=100)
    Credit_History = forms.CharField(max_length=100)
    Education = forms.CharField(max_length=100)
    Married = forms.CharField(max_length=100)
    Self_Employed  = forms.CharField(max_length=100)
    Dependents  = forms.CharField(max_length=100)
    Dependents1 = forms.CharField(max_length=100)
    
    
class TwitterMining(forms.Form):
	Search_element = forms.CharField(max_length=500)
    
class RegisterForm(forms.ModelForm) :
    class Meta():
        model = Register
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    # portfolio = forms.URLField(required = True)
    # image = forms.ImageField(required = True)

    class Meta():
        models = UserProfile
        fields = ['username','email','password']