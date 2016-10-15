from django.test import TestCase

from django.core.urlresolvers import reverse

from model_mommy import mommy

from dicadm_django.dictionary.models import Word

class WordTestCase(TestCase):
	def setUp(self):
		self.words = mommy.make('dictionary.Word', _quantity=5)
		self.word = Word.objects.all().first()

	def tearDown(self):
		Word.objects.all().delete()

	def test_create(self):
		self.assertEquals(Word.objects.count(), 5)

	def test_get_absolute_url(self):
		pass
