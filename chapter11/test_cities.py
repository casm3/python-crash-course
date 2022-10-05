import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        expected = "Santiago, Chile"
        result = city_country("santiago", "chile")
        self.assertEqual(expected, result)

    def test_city_country_population(self):
        expected = "Santiago, Chile - population 5000000"
        result = city_country("santiago", "chile", population=5_000_000)
        self.assertEqual(expected, result)
