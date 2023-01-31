from django.test import TestCase, Client
from django.urls import reverse
from register.models import AirlineSeat
import json

#  python manage.py test register.tests.test_views to only run tests in this file
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.login_url = reverse('login')
    def test_index_view_GET(self):
        response = self.client.get(reverse(self.index_url))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/index.html')

    def test_login_GET(self):
        response = self.client.get(reverse(self.login_url))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login_user.html')

    # def test_login_POST_no_data(self):
