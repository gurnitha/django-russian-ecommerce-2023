# app/home/views.py
# Django and third parties modules
from django.shortcuts import render
from django.http import HttpResponse

# Locals
from app.home.models import Setting

def index(request):
	setting = Setting.objects.get(pk=1)
	context={'setting':setting }
	return render(request, 'app/home/index.html',context)