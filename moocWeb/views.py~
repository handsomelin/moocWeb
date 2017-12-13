from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.template import RequestContext


def mainPage(request):
	#return HttpResponse('')
	students = 1
	return render_to_response('welcome.html', RequestContext(request, locals()))