from django.urls import path, include
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, lambda request: HttpResponse("Hi, welcome to Gwen's interactions endpoint server! Cookies?")),
    path('test/', lambda request: HttpResponse("Test URL works!")),
    path('interactions/', include('discord_interaction.urls')),
]
