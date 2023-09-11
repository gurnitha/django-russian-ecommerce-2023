# app/home/views.py
# Django and third parties modules
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello, World!')
