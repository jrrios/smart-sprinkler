from django.shortcuts import render

from .forms import *

# Create your views here.
def dashboard(request):
	title = "Smart Sprinkler System"
	status = True
	form = PropertyForm(request.POST or None)

	context = {
		'title': title,
		'status': status,
		'form': form,
	}

	if (request.POST):
		address_digit = int(*request.POST.get('address_digit'))
		property_type = int(*request.POST.get('property_type'))
		# super swain code here


	return render (request, 'dashboard.html', context)