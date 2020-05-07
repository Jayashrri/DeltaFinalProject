from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from newspage.models import UserPreferences

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            form.save()
            NewUser=User.objects.get(username=username)
            NewPref=UserPreferences(user_name=NewUser)
            NewPref.save()
            return HttpResponseRedirect('/accounts/login')                  
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/signup.html', {'form' : form})