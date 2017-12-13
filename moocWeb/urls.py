"""moocWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from moocWeb import views
from moocWeb.views import mainPage
from course.views import dashBoard, passrateCourse

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainPage, name='mainPage'),
	url(r'^dashBoard$', dashBoard, name='dashBoard'),
	url(r'^passrateCourse/(\d{1, 5})/$', passrateCourse, name='passrateCourse'),
]
