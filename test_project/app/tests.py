from django.test import TestCase

from .utils import random_chars, random_name, random_string


class SimpleTest(TestCase):
    def test_random_str(self):
        self.assertTrue(len(random_string()) == 30)
        self.assertNotEqual(random_chars(30), random_string())
        self.assertNotEqual(random_name(), random_name())

    def test_db(self):
        from . import models
        models.Person.objects.create(name='scott')
        cnt = models.Person.objects.count()
        print(cnt)
        self.assertTrue(cnt >= 1)

    def test_db2(self):
        from . import models
        models.Person.objects.create(name='scott')
        cnt = models.Person.objects.count()
        print(cnt)
        self.assertTrue(cnt >= 1)
