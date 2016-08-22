from django.db import models

from django.core.urlresolvers import reverse

class Word(models.Model):

	title = models.CharField('Título', max_length=120)
	slug = models.SlugField('Atalho', unique=True)
	description = models.TextField('Descrição')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("dictionary:detail", kwargs={'slug':self.slug})
		