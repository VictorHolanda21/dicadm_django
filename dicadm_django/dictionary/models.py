from django.db import models

from django.core.urlresolvers import reverse

class Category(models.Model):

	name = models.CharField('Nome', max_length=120, unique=True)
	slug = models.SlugField('Atalho', unique=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)
	
	def __str__(self):
		return self.name


class Word(models.Model):
	category = models.ForeignKey(Category)

	title = models.CharField('Título', max_length=120)
	slug = models.SlugField('Atalho', unique=True)
	description = models.TextField('Descrição')

	views = models.IntegerField('Visualizações', default=0)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("dictionary:detail", kwargs={'slug':self.slug})
		