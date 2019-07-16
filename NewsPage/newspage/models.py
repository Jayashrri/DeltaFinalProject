from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class MainSite(models.Model):
    name=models.CharField(max_length=100, help_text='Enter name of main site')

class FeedList(models.Model):
    main_site=models.ForeignKey(MainSite, on_delete=models.SET_NULL, null=True, help_text='Enter the URL of the Main Site')
    topic_name=models.CharField(max_length=100, help_text='Enter the topic of articles')
    url=models.CharField(max_length=1000, help_text='Enter URL of topic RSS Feed')

    def __str__(self):
        return f'{self.main_site.name}: {self.topic_name}'
    

class UserPreferences(models.Model):
    user_name=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    display_period=models.IntegerField(help_text='Enter number of days from which to show articles')
    articles_per_page=models.IntegerField(help_text='Enter number of articles displayed per page')
    following_sites=models.ManyToManyField(FeedList, help_text='Select sites to follow')

    def get_absolute_url(self):
        return reverse('user-prefs', args=[str(self.id)])

