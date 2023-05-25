***REMOVED***autoramosweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home'***REMOVED***
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(***REMOVED***, name='home'***REMOVED***
Including another URLconf
    1. Import the include(***REMOVED*** function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'***REMOVED***
***REMOVED***
from django.contrib import admin
from django.urls import path
from django.urls import include
from register import views as reg

urlpatterns = [
    path('admin/', admin.site.urls***REMOVED***,
    path('', include('autoramos.urls'***REMOVED***,
    path('register/', reg.register, name='register'***REMOVED***,
    path('', include("django.contrib.auth.urls"***REMOVED***,
***REMOVED***
