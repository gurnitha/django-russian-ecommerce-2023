# app/about/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from app.home.models import Setting

def about(request):
	setting = Setting.objects.get(pk=1)
	context={'setting':setting }
	return render(request, 'app/about/about.html',context)
