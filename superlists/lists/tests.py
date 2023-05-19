from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from superlists.lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')