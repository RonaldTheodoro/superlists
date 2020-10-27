from django.urls import resolve
from django.test import TestCase

from apps.lists import views


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index)
