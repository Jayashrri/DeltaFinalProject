from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class MainSite(models.Model):
    name=models.CharField(max_length=100, help_text='Enter name of main site')

    def __str__(self):
        return f'{self.name}'

class FeedList(models.Model):
    main_site=models.ForeignKey(MainSite, on_delete=models.SET_NULL, null=True, help_text='Enter the name of the Main Site')
    topic_name=models.CharField(max_length=100, help_text='Enter the topic of articles')
    url=models.CharField(max_length=1000, help_text='Enter URL of topic RSS Feed')

    def __str__(self):
        return f'{self.main_site.name}: {self.topic_name}'
    __str__.short_description='Feed Name'
    

class UserPreferences(models.Model):
    user_name=models.OneToOneField(User, on_delete=models.CASCADE)
    display_period=models.IntegerField(help_text='Enter number of days from which to show articles')
    articles_per_page=models.IntegerField(help_text='Enter number of articles displayed per page')
    following_sites=models.ManyToManyField(FeedList, help_text='Select sites to follow')

    def get_absolute_url(self):
        return reverse('user-prefs', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.user_name}'
    __str__.short_description='Username'

    def display_sites(self):
        return '\n'.join([str(sites) for sites in self.following_sites.all()])
    display_sites.short_description='Sites Following'

