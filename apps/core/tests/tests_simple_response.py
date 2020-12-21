from django.urls import reverse

from django.test import TestCase
from django.test.client import RequestFactory

from rest_framework import status

from apps.core.views import basic_response
# Create your tests here.

class SimpleResponseTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_simple_response(self):
        request = self.factory.get(reverse('basic_response'))
        basic_response_view = basic_response(request)
        response_data = basic_response_view.data['message']

        self.assertEqual(basic_response_view.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, 'Basic response!')
