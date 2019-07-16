from django.shortcuts import render
from newspage.models import MainSite, FeedList, UserPreferences

# Create your views here.

def index(request):
    return render(request, 'index.html')
