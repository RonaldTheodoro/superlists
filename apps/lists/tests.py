from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from apps.lists import views


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)

    def test_index_return_correct_html(self):
        request = HttpRequest()
        response = views.index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))