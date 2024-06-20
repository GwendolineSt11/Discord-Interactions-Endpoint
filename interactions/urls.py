from django.urls import path
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from . import views

urlpatterns = [
    path('', views.interaction_endpoint, name='interaction_endpoint'),
]
