from dataclasses import fields
from django import forms
from demoapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.forms import TextInput

class LoginForm(forms.Form):
    name = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password')

class StudentForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)
    roll_no = forms.IntegerField(label='Roll no')
    class_no = forms.IntegerField(label='class no')
    address = forms.CharField(label='Address', max_length=70)
 
 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'    

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'description']

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        
class QuizModelForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = '__all__'
        
from django import forms
from .models import Reg
class RegForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = Reg
        widgets = {'pwd': forms.PasswordInput(),}
        fields = ['user', 'pwd','fname','lname','dob','mobno']
class LoginForm(forms.Form):
    user = forms.CharField(max_length=20)
    pwd = forms.CharField(widget=forms.PasswordInput())
        
