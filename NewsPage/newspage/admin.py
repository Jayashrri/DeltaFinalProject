from django.contrib import admin
from newspage.models import MainSite, FeedList, UserPreferences

# Register your models here.

admin.site.register(MainSite)
admin.site.register(FeedList)
admin.site.register(UserPreferences)