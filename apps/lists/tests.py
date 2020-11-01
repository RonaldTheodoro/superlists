from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from apps.lists import views


class HomePageTest(TestCase):

    def test_index_return_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'index.html')
