import datetime
import unittest

from django.test import TestCase
from django.utils import timezone

from .utils.types import parseInt, parse_date, parse_date_next

class SimpleTest(unittest.TestCase):

    def test_parse_int(self):
        self.assertTrue(parseInt('123') == 123)
        self.assertTrue(parseInt('-123') == -123)
        self.assertTrue(parseInt('123asd') == 123)
        self.assertTrue(parseInt('-123asd') == -123)

    def test_parse_date(self):
        self.assertEqual(parse_date('2016-06-1', False), datetime.datetime(2016,6,1))
        self.assertEqual(parse_date('2016-06-1'), timezone.make_aware(datetime.datetime(2016,6,1), timezone.get_current_timezone()))
        self.assertEqual(parse_date('2016-12-08 23:09:25', False), datetime.datetime(2016,12,8,23,9,25))
        self.assertEqual(parse_date('2016-12-08 23:09:25'), timezone.make_aware(datetime.datetime(2016,12,8,23,9,25), timezone.get_current_timezone()))
        self.assertEqual(parse_date_next('2016-06-18', False), datetime.datetime(2016,6,19))
        self.assertEqual(parse_date_next('2016-12-31', False), datetime.datetime(2017,1,1))
        self.assertEqual(parse_date_next('2016-12-08 23:09:25', False), datetime.datetime(2016,12,8,23,9,26))
        self.assertEqual(parse_date_next('2016-12-08 23:09:59', False), datetime.datetime(2016,12,8,23,10,0))


class DbTest(TestCase):
    '''
    use TestCase to auto rollback after each test method. (see TestCase._fixture_teardown)
    '''

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
