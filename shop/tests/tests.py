from django.test import TestCase

from shop.utils import sum_price_count, CalculateMoney


class CalculateMoneyDefTestCase(TestCase):
    def test_sum_count_price_pass(self):
        result = sum_price_count(price=100, count=10)
        self.assertEquals(result, 1000)

    def test_sum_count_price_2_pass(self):
        result = sum_price_count(500, 1)
        self.assertEquals(result, 500)

    def test_sum_count_price_discount_pass(self):
        result = sum_price_count(price=200, count=15, discount=5)
        self.assertEquals(result, 2850)

class CalculateMoneyClassTestCase(TestCase, CalculateMoney):
    def test_sum_count_price_pass(self):
        result = self.sum_price_count(price=100, count=10)
        self.assertEquals(result, 1000)

    def test_sum_price_pass(self):
        list_prices = [200, 640, 720]