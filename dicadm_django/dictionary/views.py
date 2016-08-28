from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from .models import Word

# Create your views here.

def index(request):
	template_name = "dictionary/index.html"
	title = "Resultado"
	words = Word.objects.all()

	query = request.GET.get('q')
	if query: 
		words = words.filter(
				Q(title__icontains=query) |
				Q(slug__icontains=query) |
				Q(description__icontains=query)
			).distinct()

	paginator = Paginator(words, 20)
	page = request.GET.get('page')
	try:
		words = paginator.page(page)
	except PageNotAnInteger:
		words = paginator.page(1)
	except EmptyPage:
		words = paginator.page(paginator.num_pages)
		
	context = {
		'title' : title,
		'words' : words,
		'queryset' : query
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