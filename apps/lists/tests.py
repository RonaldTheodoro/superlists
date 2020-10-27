from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from apps.lists import views


class HomePageTest(TestCase):

    def test_index_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
