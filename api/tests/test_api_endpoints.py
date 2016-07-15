from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from .tests import create_test_items, create_test_companies

from api.models import *

# Create your tests here.

def create_test_bags():
    bags = {
            0: {'size':'3x3', 'mil': 4, 'top':'zip'},
            1: {'size':'4x6', 'mil': 2, 'top':'zip'},
            2: {'size':'5x7', 'mil': 4, 'top':'ziphh'},
    }
    for i in bags:
        b = Bag(size=bags[i]['size'], mil=bags[i]['mil'],
                top=bags[i]['top'])
        b.save()

def create_test_box():
    b = Box(id=1, length='10', width='10', height='10')
    b.save()

class ApiEndpointTests(APITestCase):
    def test_bag_ep(self):
        create_test_bags()
        response = self.client.get('/api/bags/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 3)
    
    def test_item_ep(self):
        create_test_items(5)
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 5)

    def test_finish_ep(self):
        create_test_companies()
        company = Company.objects.last().id
        f = Finish(id=1, name='Test Finish')
        f.save()
        r = self.client.get('/api/finishes/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(len(r.json()['results']), 1)

    def test_part_ep(self):
        create_test_items(1)
        item_rev = ItemRevision.objects.last()
        p = Part(partdesc="Test Part", size="Test Size", item_revision=item_rev,
                 origin='USA')
        p.save()
        r = self.client.get('/api/parts/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(len(r.json()['results']), 1)

    def test_kit_ep(self):
        create_test_items(1)
        create_test_bags()
        create_test_box()
        bag = Bag.objects.last()
        box = Box.objects.last()
        item_rev = ItemRevision.objects.last()
        k = Kit(kitname='Test Kit', ctnqty='90', item_revision=item_rev,
                bagtype=bag, boxtype=box)
        k.save()
        r = self.client.get('/api/kits/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(len(r.json()['results']), 1)

    def test_box_ep(self):
        create_test_box()
        r = self.client.get('/api/boxes/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(len(r.json()['results']), 1)
       
    def test_uom_ep(self):
        u = Uom(name="Pieces", abbrv='pcs')
        u.save()
        r = self.client.get('/api/uoms/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(len(r.json()['results']), 1)
