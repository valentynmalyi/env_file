from django.test import TestCase
from django.conf import settings


class ShowJson(TestCase):
    def test_key_hello(self):
        self.assertIn("hello", settings.SHOW_DATA)

    def test_obvious(self):
        self.assertIsNone(None)
