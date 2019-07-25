from django.shortcuts import render, redirect
from newspage.models import FeedList, UserPreferences, FeedListForm, SavedArticles
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

def index(request):
    return render(request, 'index.html')

def DispFeed(request, pk):
    FeedName=FeedList.objects.get(id=pk)
    Feed=rss.GetFeed(FeedName)
    FeedName.last_update=datetime.datetime.now()
    FeedName.save()
    return render(request, 'feed.html', context={'Feed': Feed, 'Name': FeedName, 'id': pk})

def DispArticle(request, feed, index):
    if(request.POST.get('addart')):
        arturl=request.POST.get('arturl')
        arttitle=request.POST.get('arttitle')
        id=request.POST.get('feedid')
        currentuser=request.user
        NewSaved=SavedArticles(saved_user=currentuser, article_url=arturl, article_title=arttitle)
        NewSaved.save()
        return redirect('feed', pk=id)
    else:
        FeedName=FeedList.objects.get(id=feed)
        FeedSet=rss.GetFeed(FeedName)
        link=FeedSet.entries[index]['link']
        article=rss.GetArticle(link,request)
        return render(request, 'article.html', context={'article': article, 'id': feed, 'url': link})

def AddFeed(request):
    if request.method == "POST":
        form = FeedListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-prefs', pk=request.user.pk)
    else:
        form=FeedListForm()
        return render(request, 'preferences_form.html', context={'form': form})

def ShowSaved(request):
    currentuser=request.user
    savedarts=SavedArticles.objects.filter(saved_user=currentuser)
    return render(request, 'saved_list.html', context={'artset': savedarts})

def DispSavedArt(request, pk):
    if(request.POST.get('addart')):
        DelArt=SavedArticles.objects.get(id=pk)
        DelArt.delete()
        return redirect('savedlist')
    else:
        saved=SavedArticles.objects.get(id=pk)
        link=saved.article_url
        article=rss.GetArticle(link,request)
        return render(request, 'saved_article.html', context={'article': article})
