import os


# configuração vista em tango with django 1.9

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
				'dicadm_django.settings')

import django
django.setup()

from dicadm_django.dictionary.models import Category, Word

def populate():
	# First, we will create lists of dictionaries containing the words
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories.
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models.

	# e.g. Administração Financeira
	# af_words = [
	# 	{
	# 		"title": "Balanço Patrimonial BP", 
	# 		"slug": "balanco-patrimonial-bp", 
	# 		"description" :"É a demonstração contábil que tem por finalidade apresentar a situação patrimonial da empresa em determinado momento, e a sua composição e apresentação seguem o ritual definido pelo Conselho Federal de Contabilidade e pela Legislação Comercial, quanto à sua forma e à necessidade de serem elaborados por um profissional legalmente habilitado, para se ter credibilidade necessária junto aos órgãos  públicos,  instituições  financeiras  e  até  mesmo  aos  fornecedores."
	# 	},
	# ]

	# Administração Geral
	ag_words = [
		{"title": "Adhocracia", "slug": "adhocracia", "description" :"Segundo Mintzberg, a Adhocracia representa estruturas fluidas e de pequena escala. Típica em equipes de projetos, esta estrutura normalmente está ligada à horizontalidade do poder de decisão. O grau de especialidade e conhecimentos são elevados e a informalidade é uma forte característica. As principais vantagens desta estrutura são a reduzida burocracia e a rapidez no processo decisório. Parte chave da organização: Assessoria de Apoio."	},
		{"title": "Administração", "slug": "administracao", "description" :"A palavra Administração vem do latim, ad– que significa direção, tendência para, e minister – que significa subordinação ou obediência, ou seja, quem realiza uma função sob comando de outra ou presta serviço a outro, (CHIAVENATO, 2003)."},
	]

	# Administração Financeira
	af_words = [
		{"title": "Balanço Patrimonial BP", "slug": "balanco-patrimonial-bp", "description" :"É a demonstração contábil que tem por finalidade apresentar a situação patrimonial da empresa em determinado momento, e a sua composição e apresentação seguem o ritual definido pelo Conselho Federal de Contabilidade e pela Legislação Comercial, quanto à sua forma e à necessidade de serem elaborados por um profissional legalmente habilitado, para se ter credibilidade necessária junto aos órgãos  públicos,  instituições  financeiras  e  até  mesmo  aos  fornecedores."},
		{"title" :"Capital de giro", "slug" :"capital-de-giro", "description" :"É o valor que a empresa necessita para cobrir seus gastos, antes da entrada dos recursos provenientes das vendas."},
	]

	# Administração de TI
	ati_words = [
		{"title": "BI Business Intelligence", "slug": "bi-business-intelligence", "description" :"É a coleta, organização e análise de informações que ajudam na gestão do negócio. Normalmente é realizado com apoio de softwares especialistas que ajudam na consolidação das informações e nas tomadas de decisões."},
		{"title" :"Governança de TI", "slug" :"governanca-de-ti", "description" :"Estrutura de relações e processos que dirige e controla uma organização de TI a fim de atingir seu objetivo de adicionar valor ao negócio através do gerenciamento balanceado do risco com o retorno do investimento em tecnologia."},
	]

	# Administração Estratégia
	ae_words =[
		{"title" :"BSC Balanced Scorecard", "slug" :"bsc-balanced-scorecard", "description" :"É uma metodologia de medição e avaliação das alternativas estratégicas, desenvolvida pelos norte-americanos Robert Kaplan e David Norton. Têm como objetivos desta metodologia: simplificar a estratégia e a sua comunicação a todos os membros da organização; alinhar a organização com a estratégia; ligar a estratégia ao plano e ao orçamento anual e medir a eficácia da estratégia. É estruturada em torno de quatro questões (ou dimensões) centrais: Perspectiva do Cliente, Perspectiva dos Processos, Perspectiva Financeira e Perspectiva da Aprendizagem e Crescimento."},
	]

	# Administração de Marketing
	mk_words = [
		{"title" :"Market share","slug" :"market-share","description" :"﻿\"Participação de mercado, em português, e é a fatia ou quota de mercado que uma empresa tem no seu segmento ou no segmento de um determinado produto. O Market Share serve para avaliar a força e as dificuldades de uma empresa, além da aceitação dos seus produtos.\""},
		{"title" :"Marketing","slug" :"marketing","description" :"Estabelece relações entre a organização e seus clientes. Abrange as diferentes atividades de pesquisa e desenvolvimento de produtos, distribuição, preço, e promoção (publicidade e propaganda)."},
	]

	cats = {
				"Geral": {"slug": "geral", "words": ag_words},
				"Financeira": {"slug": "financeira", "words": af_words},
				"Tecnologia da Informação": {"slug": "tecnologia-da-informacao", "words": ati_words},
				"Estratégia" : {"slug":"estrategia", "words":ae_words},
				"Marketing": {"slug": "marketing", "words": mk_words},
			}


	# The code below goes through the cats dictionary, then adds each category,
	# and then adds all the associated words for that category.

	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data)
		for p in cat_data["words"]:
			add_word(c, p["title"], p["slug"], p["description"])


	# Print
	for c in Category.objects.all():
		for p in Word.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))


def add_word(cat, title, slug, description, views=0):
	p = Word.objects.get_or_create(category=cat, title=title)[0]
	p.slug = slug
	p.description = description
	p.save()
	return p


def add_cat(name, cat_data):
	c = Category.objects.get_or_create(name=name)[0]
	c.slug = cat_data["slug"]
	c.save()
	return c


# Start execution here!

if __name__ == '__main__':
	print("Iniciando script... \nPopulação do Banco de Dados de DICADM APP........")
	populate()
	cats, words = Category.objects.count(), Word.objects.count()
	print("\nFim do script.....")
	print("Categorias adiciondas: {0} \nPalavras adiciondas: {1}".format(cats, words))
