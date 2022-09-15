import datetime
from django.test import TestCase

from Finance import queries
from Finance import models
from decimal import Decimal


class QueryTest(TestCase):
    fixtures = ['auth_sample.json', 'data_sample.json']

    def test_sample_query_1(self):
        p = queries.query_1()
        self.assertTrue('total_dept' in p.keys())
        self.assertEqual(float(Decimal(69806.5300000000000)), float(p['total_dept']))

    def test_sample_query_2(self):
        p = queries.query_2(10)
        self.assertTrue('total_overtime' in p.keys())
        self.assertEqual(float(Decimal(9537)), float(p['total_overtime']))

    def test_sample_query_3(self):
        p = queries.query_3()
        self.assertTrue('total' in p.keys())
        self.assertEqual(float(Decimal(62220.7200000000)), float(p['total']))

    def test_sample_query_4(self):
        pks = [x for x in models.Employee.objects.values('pk')[:20]]
        ans = {114: None, 117: None, 119: 19, 121: 1, 123: 55, 127: None, 106: None, 107: None, 111: None, 122: None, 132: 16, 116: 38, 126: None, 130: None, 118: None, 120: None, 128: None, 131: None, 108: None, 109: None}
        for pk in pks:
            p = queries.query_4(pk['pk'])
            self.assertEqual(type(dict()), type(p))
            self.assertTrue('total_hours' in p.keys())
            self.assertEqual(p['total_hours'], ans[pk['pk']])

    def test_sample_query_5(self):
        total_salary = 1000
        q = models.Employee.objects.filter(pk__in=[119,128,111,112])
        p = queries.query_5(total_salary)
        self.assertEqual(p.count(), q.count())
        self.assertEqual(type(q), type(p))
        self.assertEqual(sorted(list(p), key=lambda emp: emp.pk), sorted(list(q), key=lambda emp: emp.pk))

    def test_sample_query_6(self):
        p = queries.query_6()
        self.assertEqual(type(p), type(models.Employee.objects.first()))
        self.assertEqual(p.total_hours, 142)

    def test_sample_query_7(self):
        p = queries.query_7()
        self.assertEqual(type(p), type(models.Department.objects.first()))
        self.assertEqual(p.total, 1793)

    def test_sample_query_8(self):
        p = queries.query_8()
        self.assertEqual(p, models.Department.objects.filter(name="Vinder").first())

    def test_sample_query_9(self):
        in_time = datetime.time(9, 0, 0)
        p = queries.query_9(in_time)
        self.assertEqual(p, models.Employee.objects.filter(account__username="Carmelia").first())

    def test_sample_query_10(self):
        p = queries.query_10()
        self.assertTrue('total' in p.keys())
        self.assertEqual(int(23), int(p['total']))
