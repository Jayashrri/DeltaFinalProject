from django.shortcuts import render
from newspage.models import MainSite, FeedList, UserPreferences
from django.views.generic import DetailView

# Create your views here.

def index(request):
    return render(request, 'index.html')

class UserPreferencesDetail(DetailView):
    model=UserPreferences
    template_name='preferences_detail.html'