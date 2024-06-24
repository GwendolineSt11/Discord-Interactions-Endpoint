from django.urls import path
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', lambda request: HttpResponse("Test URL works!")),
    path('interactions/', include('interactions.urls')),
    path('', views.interactions_view, name='interactions'),
]
