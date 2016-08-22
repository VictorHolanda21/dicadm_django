from django.shortcuts import render

# Create your views here.

def index(request):
	template_name = "dictionary/index.html"
	title = "Termos"

	context = {
		'title' : title,
	}
	return render(request, template_name, context)

def word(request):
	template_name = "dictionary/word.html"
	title = "Termo"

	context = {
		'title' : title,
	}
	return render(request, template_name, context)