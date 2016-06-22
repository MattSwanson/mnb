from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

class SimpleTests(TestCase):
    def test_variable_assignment(self):
        x = 1
        self.assertEqual(x,1)

class InitViewTests(TestCase):
    def test_index(self):
        response = self.client.get(reverse('web:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the beginning...")
