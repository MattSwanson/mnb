from rest_framework import status
from rest_framework.test import APITestCase

class ApiRootTest(APITestCase):
    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
