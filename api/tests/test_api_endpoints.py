from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from .tests import create_test_items

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
