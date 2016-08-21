from django.shortcuts import render

# Create your views here.

def index(request):
	template_name = "core/index.html"
	title = "Início"

	context = {
		'title' : title
	}
	return render(request, template_name, context)

def about(request):
	template_name = "core/about.html"
	title = "Início"

	context = {
		'title' : title
	}
	return render(request, template_name, context)