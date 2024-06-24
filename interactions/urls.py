from django.urls import path, include
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', lambda request: HttpResponse("Test URL works!")),
    path('interactions/', views.interactions_view, name='interactions'),
]
