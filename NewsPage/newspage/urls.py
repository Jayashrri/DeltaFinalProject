from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preferences/<int:pk>', views.UserPreferencesDetail.as_view(), name='user-prefs'),
]