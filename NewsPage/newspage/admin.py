from django.contrib import admin
from newspage.models import FeedList, UserPreferences, SavedArticles

# Register your models here.

@admin.register(FeedList)
class FeedListAdmin(admin.ModelAdmin):
    list_display=['__str__','url']

@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display=['__str__','display_sites']

@admin.register(SavedArticles)
class SavedArticlesAdmin(admin.ModelAdmin):
    list_display=['saved_user','article_title','article_url']
