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

    if request.POST and form.is_valid():
        operation = Operations()
        current_temp, recent_precip, forecast_precip = operation.get_weather()

        if form.is_valid():
            conditions = {
                "current_temp": current_temp,
                "recent_precip": recent_precip,
                "forecast_precip": forecast_precip,

            }

            context ["conditions"]=conditions
            context['restrictions'] = operation.get_water_restrictions(
                form.cleaned_data['address_digit'],
                form.cleaned_data['property_type']
            )

            print conditions

    return render (request, 'dashboard.html', context)