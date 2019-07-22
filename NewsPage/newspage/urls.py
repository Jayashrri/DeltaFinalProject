from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedUpdate, name='index'),
    path('preferences/<int:pk>', views.UserPreferencesDetail.as_view(), name='user-prefs'),
    path('preferences/<int:pk>/update/', views.UserPreferencesUpdate.as_view(), name='user-prefs-update'),
    path('topics/<int:pk>', views.DispTopics.as_view(), name='topics'),
    path('topics/viewfeed/<int:pk>', views.DispFeed, name='feed'),
    path('topics/article/<int:feed>/<int:index>', views.DispArticle, name='articles'),
]