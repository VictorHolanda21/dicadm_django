from django.test import TestCase, Client

from django.core.urlresolvers import reverse

class IndexTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.url = reverse('dictionary:index')

	def tearDown(self):
		pass

	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'dictionary/index.html')

	def test_context(self):
		response = self.client.get(self.url)
		self.assertTrue('title' in response.context)
		self.assertEquals(response.context['title'], "Termos" )

class WordTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.url = reverse('dictionary:word')

	def tearDown(self):
		pass

	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'dictionary/word.html')

	def test_context(self):
		response = self.client.get(self.url)
		self.assertTrue('title' in response.context)
		self.assertEquals(response.context['title'], "Termo" )