from django.test import TestCase, Client

from django.core.urlresolvers import reverse

# Create your tests here.


class IndexTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.url = reverse('core:index')

	def tearDown(self):
		pass

	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'core/index.html')



class AboutTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.url = reverse('core:about')

	def tearDown(self):
		pass

	def test_status_code(self):
		response = self.client.get(self.url)
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get(self.url)
		self.assertTemplateUsed(response, 'core/about.html')