from django.shortcuts import render

# Create your views here.
def dashboard(request):
	title = "Smart Sprinkler System"
	status = True

	context = {
		'title': title,
		'status': status,
	}

	return render (request, 'dashboard.html', context)