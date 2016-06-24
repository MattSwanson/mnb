from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone


from api.models import *

# Create your tests here.


# create_test_items(qty) 
# This will create qty number of items for testing purposes
# The item numbers will be of the format 'TestItem<i>' 
# Each item will also have 3 item revisions generated for it as well
def create_test_items(qty):
    test_company = Company(name='TestCo', vmi=0)
    test_company.save()
    test_vendor = Vendor(company=test_company)
    test_vendor.save()
    test_uom = Uom(name='Pieces', abbrv = 'pcs')
    test_uom.save()
    date = timezone.now()
    
    for i in range(1,qty+1):
        item_number = 'TestItem%i' % (i)
        item = Item(item_number=item_number, pref_vendor=test_vendor, def_uom=test_uom)
        item.save()
        for j in range(1,4):
            rev_name = '0%i' % (j)
            item_revision = ItemRevision(name=rev_name, item=item, eff_date=date)
            item_revision.save()


class TestFunctionTests(TestCase):
    def test_create_test_items(self):
        create_test_items(3)
        exp_items_qs = ['<Item: TestItem1>', '<Item: TestItem2>', '<Item: TestItem3>']
        exp_item_revs_qs = [
            '<ItemRevision: TestItem1 01>',
            '<ItemRevision: TestItem1 02>',
            '<ItemRevision: TestItem1 03>',
            '<ItemRevision: TestItem2 01>',
            '<ItemRevision: TestItem2 02>',
            '<ItemRevision: TestItem2 03>',
            '<ItemRevision: TestItem3 01>',
            '<ItemRevision: TestItem3 02>',
            '<ItemRevision: TestItem3 03>'
        ]
        items = Item.objects.all().order_by('item_number')
        item_revisions = ItemRevision.objects.all().order_by('pk')
        self.assertQuerysetEqual(items, exp_items_qs)
        self.assertQuerysetEqual(item_revisions, exp_item_revs_qs)




class SimpleTests(TestCase):
    def test_variable_assignment(self):
        x = 1
        self.assertEqual(x,1)

class InitViewTests(TestCase):
    def test_index(self):
        response = self.client.get(reverse('api:index'))
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
