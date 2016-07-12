from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone


from api.models import *

# Create your tests here.


def create_test_uoms():
    uoms = { 
            0: {'name':'Pounds', 'abbrv':'lbs'},
            1: {'name':'Pieces', 'abbrv':'pcs'},
            2: {'name':'Inches', 'abbrv':'in'},
            3: {'name':'Feet', 'abbrv':'ft'},
    }
    for i in uoms:
        u = Uom(name=uoms[i]['name'], abbrv=uoms[i]['abbrv'])
        u.save()

# Create some test companies for use with various models for testing
def create_test_companies():
    for i in range(1,6):
        name = 'Test Company %i' % (i)
        company = Company(name=name, vmi=0)
        company.save()
    # Make a couple vendors out of the last 2 companies
    for c in Company.objects.all().order_by('pk')[3:5]:
        vendor = Vendor(company=c)
        vendor.save()

# create_test_items(qty) 
# This will create qty number of items for testing purposes
# The item numbers will be of the format 'TestItem<i>' 
# Each item will also have 3 item revisions generated for it as well
def create_test_items(qty):
    create_test_companies()
    create_test_uoms()
    uom = Uom.objects.first()
    date = timezone.now()
    
    for i in range(1,qty+1):
        item_number = 'TestItem%i' % (i)
        item = Item(item_number=item_number, def_uom=uom)
        item.save()
        for j in range(1,4):
            rev_name = '0%i' % (j)
            item_revision = ItemRevision(name=rev_name, item=item, eff_date=date)
            item_revision.save()


class TestFunctionTests(TestCase):
    # Ensure test items are being created properly
    def test_create_test_items(self):
        create_test_items(3) 
        items = Item.objects.all()
        item_revisions = ItemRevision.objects.all()
        self.assertEqual(items.count(), 3)
        self.assertEqual(item_revisions.count(), 9)

    # Ensure test companies are being created properly
    def test_create_test_companies(self):
        create_test_companies()
        exp_companies_qs = [
            '<Company: Test Company 1>',
            '<Company: Test Company 2>',
            '<Company: Test Company 3>',
            '<Company: Test Company 4>',
            '<Company: Test Company 5>',
        ]
        exp_vendors_qs = [
            '<Vendor: Test Company 4>',
            '<Vendor: Test Company 5>',
        ]
        companies = Company.objects.all().order_by('pk')
        vendors = Vendor.objects.all().order_by('pk')
        self.assertQuerysetEqual(companies, exp_companies_qs)
        self.assertQuerysetEqual(vendors, exp_vendors_qs)

class SimpleTests(TestCase):
    def test_variable_assignment(self):
        x = 1
        self.assertEqual(x,1)

class BagModelTests(TestCase):
    def test_str(self):
        bag = Bag(size='3x3', mil=4, top='zip')
        self.assertEqual(bag.__str__(), '3x3 zip 4mil')

class BoxModelTests(TestCase):
    def test_str(self):
        box = Box(length=16, width=12, height=9)
        self.assertEqual(box.__str__(), '16x12x9')


class ItemModelTests(TestCase):
    def test_str(self):
        item_num = 'Test123'
        item = Item(item_number=item_num)
        self.assertEqual(item.__str__(), item_num)


class ItemRevisionModelTests(TestCase):
    def test_str(self):
        item_num = 'Test123'
        rev_name = '01'
        eff_date = '2016-07-01'
        item = Item(item_number=item_num)
        item_rev = ItemRevision(item=item, name=rev_name, eff_date=eff_date)
        s = '%s - %s' % (rev_name, eff_date)
        self.assertEquals(item_rev.__str__(), s) 

class OrderlineModelTests(TestCase):
    def test_str_shows_qty_item_number_rev_name_po(self):
        qty = 100
        item_number = 'TestItem1'
        item_rev = '01'
        po_number = 'TestPO1'
        item = Item(item_number=item_number)
        item_revision = ItemRevision(item=item, name=item_rev)
        customer = Company(name='Test Company')
        order = Order(custid=customer, custpo=po_number)
        orderline = Orderline(quantity=qty, item_rev=item_revision, o=order)
        s = '%i %s Rev: %s on PO %s' % (qty, item_number, item_rev, po_number)
        self.assertEquals(orderline.__str__(), s)

class UserModelTests(TestCase):
    def test_str_shows_full_name_and_email(self):
        first_name = 'Test'
        last_name = 'Person'
        email = 'test@aol.com'
        user = User(lastname=last_name, firstname=first_name, email=email)
        s = '%s, %s - %s' % (last_name, first_name, email)
        self.assertEquals(user.__str__(), s)


       
