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
from course.views import dashBoard, passrateCourse, ratingCourse, registerCourse, studentCourse, passrateItem, ratingItem, registerWeeklyItem, registerDailyItem, download, download2, download3, download4, download5, download6, download7, download1

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainPage, name='mainPage'),
	url(r'^dashBoard/$', dashBoard, name='dashBoard'),
	url(r'^passrateCourse/(\d{1,5})/$', passrateCourse, name='passrate_course'),
    url(r'^ratingCourse/(\d{1,5})/$', ratingCourse, name='rating_course'),
    url(r'^registerCourse/(\d{1,5})/$', registerCourse, name='register_course'),
    url(r'^studentCourse/(\d{1,5})/$', studentCourse, name='student_course'),
    url(r'^passrateItem/(\d{1,5})/$', passrateItem, name='passrate_item'),
    url(r'^ratingItem/(\d{1,5})/$', ratingItem, name='rating_item'),
    url(r'^registerWeeklyItem/(\d{1,5})/$', registerWeeklyItem, name='register_weekly_item'),
    url(r'^registerDailyItem/(\d{1,5})/$', registerDailyItem, name='register_daily_item'),
    url(r'^download/(\d{1,5})/$', download, name='download'),
    url(r'^download1/(\d{1,5})/$', download1, name='download1'),
    url(r'^download2/(\d{1,5})/$', download2, name='download2'),
    url(r'^download3/(\d{1,5})/$', download3, name='download3'),
    url(r'^download4/(\d{1,5})/$', download4, name='download4'),
    url(r'^download5/(\d{1,5})/$', download5, name='download5'),
    url(r'^download6/(\d{1,5})/$', download6, name='download6'),
    url(r'^download7/(\d{1,5})/$', download7, name='download7'),
]
