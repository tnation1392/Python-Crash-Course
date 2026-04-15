import unittest
#import the function for testing
from names_function import get_formatted_name

#Create a class for testing
class NamesTestCase(unittest.TestCase):
    def test_first_last(self):
        #Does a name like Jimi Hendrix work?
        formatted_name = get_formatted_name("jimi","","hendrix")
        self.assertEqual(formatted_name, "Jimi Hendrix")

    def test_first_middle_last(self):
        #Would a name like John F. Kennedy work?
        formatted_name = get_formatted_name(
            "john", "f", "kennedy")
        self.assertEqual(formatted_name, "John F Kennedy")

if __name__ == '__main__':
    unittest.main()