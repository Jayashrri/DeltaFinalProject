from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from newspage.models import UserPreferences

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists()):
                User.objects.create_user(username, password)
                NewUser=User.objects.get(username=username)
                NewPref=UserPreferences(user_name=NewUser, display_period=2, articles_per_page=10)
                NewPref.save()
                return HttpResponseRedirect('/accounts/login')    
            else:
                raise forms.ValidationError('User with that username already exists.')
                
    else:
        form = UserRegistrationForm()
        
    return render(request, 'registration/signup.html', {'form' : form})