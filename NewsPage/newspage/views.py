from django.shortcuts import render
from newspage.models import MainSite, FeedList, UserPreferences
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from . import rss
import datetime

# Create your views here.

class UserPreferencesDetail(DetailView):
    model=UserPreferences
    template_name='preferences_detail.html'

class UserPreferencesUpdate(UpdateView):
    model=UserPreferences
    template_name='preferences_form.html'
    fields=['following_sites']

class DispTopics(DetailView):
    model=UserPreferences
    template_name='topic_list.html'

def DispFeed(request, pk):
    FeedName=FeedList.objects.get(id=pk)
    Feed=rss.GetFeed(FeedName)
    FeedName.last_update=datetime.datetime.now()
    FeedName.save()
    return render(request, 'feed.html', context={'Feed': Feed, 'Name': FeedName, 'id': pk})

def DispArticle(request, feed, index):
    FeedName=FeedList.objects.get(id=feed)
    FeedSet=rss.GetFeed(FeedName)
    link=FeedSet.entries[index]['link']
    article=rss.GetArticle(link,request)
    return render(request, 'article.html', context={'article': article, 'id': feed})

def FeedUpdate(request):
    IsUpdated=[]
    FeedItems=FeedList.objects.all()
    for FeedItem in FeedItems:
        result=rss.CheckUpdate(FeedItem)
        if (result):
            IsUpdated.append(FeedItem)
    return render(request, 'index.html', context={'isupdated': IsUpdated})
