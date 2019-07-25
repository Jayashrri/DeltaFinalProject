from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# Create your models here.

class FeedList(models.Model):
    main_site=models.CharField(max_length=100, help_text='Enter the name of the Main Site')
    topic_name=models.CharField(max_length=100, help_text='Enter the topic of articles')
    url=models.CharField(max_length=1000, help_text='Enter URL of topic RSS Feed')

    def __str__(self):
        return f'{self.main_site}: {self.topic_name}'
    __str__.short_description='Feed Name'

    class Meta:
        verbose_name='Feed List'
    

class UserPreferences(models.Model):
    user_name=models.OneToOneField(User, on_delete=models.CASCADE)
    following_sites=models.ManyToManyField(FeedList, help_text='Select sites to follow', blank=True)

    def get_absolute_url(self):
        return reverse('user-prefs', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.user_name}'
    __str__.short_description='Username'

    def display_sites(self):
        return '\n'.join([str(sites) for sites in self.following_sites.all()])
    display_sites.short_description='Sites Following'

    class Meta:
        verbose_name='User Preference'
        verbose_name_plural='User Preferences'

class SavedArticles(models.Model):
    saved_user=models.ForeignKey(User, on_delete=models.CASCADE)
    article_url=models.TextField()
    article_title=models.TextField()

    class Meta:
        verbose_name='Saved Article'

class FeedListForm(forms.ModelForm):
    class Meta:
        model=FeedList
        fields=['main_site','topic_name','url']