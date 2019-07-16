from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', RedirectView.as_view(url='/', permanent=True)),
]