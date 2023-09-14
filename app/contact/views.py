# app/contact/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals

def contact(request):
	return render(request, 'app/contact/contact.html')

