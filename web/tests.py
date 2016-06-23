from django.test import TestCase
from django.core.urlresolvers import reverse

from web.models import *

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

class ItemModelTests(TestCase):
    def test_str(self):
        item_num = 'Test123'
        item = Item(item_number=item_num)
        self.assertEqual(item.__str__(), item_num)


class ItemRevisionModelTests(TestCase):
    def test_str(self):
        item_num = 'Test123'
        rev_name = '01'
        item = Item(item_number=item_num)
        item_rev = ItemRevision(item=item, name=rev_name)
        s = '%s %s' % (item_num, rev_name)
        self.assertEquals(item_rev.__str__(), s) 

class UserModelTests(TestCase):
    def test_str_shows_full_name_and_email(self):
        first_name = 'Test'
        last_name = 'Person'
        email = 'test@aol.com'
        user = User(lastname=last_name, firstname=first_name, email=email)
        s = '%s, %s - %s' % (last_name, first_name, email)
        self.assertEquals(user.__str__(), s)
