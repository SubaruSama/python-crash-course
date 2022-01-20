import unittest
from CityCountry import city_country

class TestCityCountr(unittest.TestCase):
    """Test case to test the functions from CityCountry."""

    def test_city_country(self) -> None:
        """This function should return City, Country formatted. Example: Santiago, Chile"""
        """TODO: When there are 'de' or separators in the city name, it breaks. Eg: rio de janeiro should return Rio de Janeiro, not Rio De Janeiro"""
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self) -> None:
        formatted_city_country_population = city_country('santiago', 'chile', '5000000')
        self.assertEqual(formatted_city_country_population, 'Santiago, Chile - population - 5000000')

unittest.main()