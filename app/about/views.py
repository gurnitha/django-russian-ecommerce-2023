# app/about/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals

def about(request):
	return render(request, 'app/about/about.html')
