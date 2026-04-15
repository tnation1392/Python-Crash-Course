import unittest
#import the function for testing
from city_function import city_country

class Test_city_country(unittest.TestCase):
    def test_city_country(self):
    #Can Hancock, Maine and United States work?
        formatted_name = city_country("hancock", "maine",
                                  "United States")
        self.assertEqual(formatted_name, "Hancock, Maine, United States")
