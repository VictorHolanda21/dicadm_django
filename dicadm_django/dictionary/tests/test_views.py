from django.test import TestCase, Client

from django.core.urlresolvers import reverse

from model_mommy import mommy

from dicadm_django.dictionary.models import Word

class IndexTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.words = mommy.make(Word, _quantity=5)
		self.url = reverse('dictionary:index')

	def tearDown(self):
		Word.objects.all().delete()

	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'dictionary/index.html')

	def test_context(self):
		response = self.client.get(self.url)
		self.assertTrue('title' in response.context)
		self.assertTrue('words' in response.context)
		self.assertEquals(response.context['title'], "Resultado" )


class DetailTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.words = mommy.make(Word, _quantity=5)
		self.word = Word.objects.all().first()
		self.url = reverse('dictionary:detail', kwargs={'slug':self.word.slug})

	def tearDown(self):
		Word.objects.all().delete()

	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'dictionary/detail.html')

	def test_context(self):
		response = self.client.get(self.url)
		self.assertTrue('title' in response.context)
		self.assertTrue('word' in response.context)
		self.assertEquals(response.context['title'], "Detalhe" )
		self.assertEquals(response.context['word'], self.word )