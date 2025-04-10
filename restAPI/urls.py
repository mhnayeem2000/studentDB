
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('api/v1/',include('api.urls')),
]
