from django.shortcuts import render
from sprinkler_operations.operations import Operations
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

		current_temp, recent_precip, forecast_precip = Operations.get_weather()

		if (form.is_valid()):
			conditions = {
				"current_temp": current_temp,
				"recent_precip": recent_precip,
				"forecast_precip": forecast_precip,
				 
			}

			context ["conditions"]=conditions

			print conditions

	return render (request, 'dashboard.html', context)