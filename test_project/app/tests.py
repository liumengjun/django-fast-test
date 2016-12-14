from django.test import TestCase

from .utils import random_chars, random_name, random_string


class SimpleTest(TestCase):
    def test_random_str(self):
        self.assertTrue(len(random_string()) == 30)
        self.assertNotEqual(random_chars(30), random_string())
        self.assertNotEqual(random_name(), random_name())
