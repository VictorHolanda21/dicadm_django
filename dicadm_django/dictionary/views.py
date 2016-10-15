from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from .models import Word, Category

from .forms import CategoryForm, WordForm

# Create your views here.

def index(request):
	template_name = "dictionary/index.html"
	title = "Dicionário"
	words = Word.objects.all()

	query = request.GET.get('q')

	if query:
		words = words.filter(
				Q(title__icontains=query) |
				Q(slug__icontains=query) |
				Q(category__name__icontains=query) | 
				Q(category__slug__icontains=query)
			).distinct()

	paginator = Paginator(words, 5)
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


def add_word(request):
	template_name = "dictionary/add_word.html"
	title = "Adicionar Termo"

	form = WordForm()
	if request.method == 'POST' :
		form = WordForm(request.POST)
		if form.is_valid():	
			word = form.save(commit=False)
			word.views = 0
			word.save()
			return detail(request, word.slug)
	else:
		print(form.errors)

	context = {
		'form' : form,
		'title' : title
	}

	return render(request, template_name, context)		


def show_category(request, slug=None):
	template_name = "dictionary/index.html"
	title = "Categorias"
	if slug:
		cat = Category.objects.get(slug=slug)
		words = Word.objects.filter(category=cat)
	else: 
		cat = ""
		words = Word.objects.all()

	paginator = Paginator(words, 5)
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
		'category' : cat
	}
	return render(request, template_name, context)


def add_category(request):
	template_name = "dictionary/add_category.html"
	title = "Adicionar categoria"
	form = CategoryForm()


	# HTTP POST
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		# Formulario válido?
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)

	context = {
		'title' : title,
		'form' : form
	}

	return render(request, template_name, context)