from django.shortcuts import render

from .models import Word

# Create your views here.

def index(request):
	template_name = "dictionary/index.html"
	title = "Termos"
	words = Word.objects.all()

	context = {
		'title' : title,
		'words' : words
	}
	return render(request, template_name, context)

def detail(request, slug):
	template_name = "dictionary/detail.html"
	title = "Detalhe"
	word = Word.objects.get(slug=slug)

	context = {
		'title' : title,
		'word' : word
	}
	return render(request, template_name, context)