from django.test import TestCase

from django.core.urlresolvers import reverse

from model_mommy import mommy

from dicadm_django.dictionary.models import Word, Category

class WordTestCase(TestCase):
	def setUp(self):
		self.words = mommy.make('dictionary.Word', _quantity=5)
		self.word = Word.objects.all().first()
		self.url = reverse('dictionary:detail', kwargs={'slug':self.word.slug})

	def tearDown(self):
		Word.objects.all().delete()

	def test_create(self):
		self.assertEquals(Word.objects.count(), 5)

	def test_get_absolute_url(self):
		absolute_url = '/dicionario/termos/{0}/'.format(self.word.slug)
		self.assertEquals(self.url, absolute_url)

class CategoryTestCase(TestCase):
	def setUp(self):
		self.categories = mommy.make('dictionary.Category', _quantity=5)
		self.cat = Category.objects.all().first()
		self.url = reverse('dictionary:show_category', kwargs={'slug':self.cat.slug})
		
	def tearDown(self):
		Category.objects.all().delete()

	def test_create(self):
		self.assertEquals(Category.objects.count(), 5)	

	def test_get_absolute_url(self):
		absolute_url = '/dicionario/categoria/{0}/'.format(self.cat.slug)
		self.assertEquals(self.url, absolute_url)