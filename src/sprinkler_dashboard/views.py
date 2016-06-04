from django.shortcuts import render

# Create your views here.
def dashboard(request):
	title = "Smart Sprinkler System"

	context = {
		'title': title,
	}
	return render (request, 'dashboard.html', context)