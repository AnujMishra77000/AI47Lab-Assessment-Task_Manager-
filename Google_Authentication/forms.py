from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from .models import Task
from django.utils.translation import gettext, gettext_lazy as _



class SignupForm(UserCreationForm):
 password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name','email']
    labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
    widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
               'first_name':forms.TextInput(attrs={'class':'form-control'}),
               'last_name':forms.TextInput(attrs={'class':'form-control'}),
               'email':forms.EmailInput(attrs={'class':'form-control'})
               
               }

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields =['Task_title','Task_description']
    lables = {'title':'Task_title', 'description':'Task_Description'}
    widgets = {'Task_title':forms.TextInput(attrs={'class':'form-control'}),
               'Task_description':forms.Textarea(attrs={'class':'form-control'})}
    

class LoginForm(AuthenticationForm): #this is makes uisng formApi , thats why we dont need models here.
   username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
   password = forms.CharField(label=_("password"), strip=False, widget= forms.PasswordInput
                              (attrs={'autofocus': True, 'class':'form-control'})
                              ) 
   


class EmailForm(forms.Form):
     email = forms.EmailField(
        label="Enter Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter recipient email',
        })
    )