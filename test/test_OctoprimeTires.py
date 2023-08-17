import unittest
from tire.OctoprimeTires import OctoprimeTires

class testOctoprimeTires(unittest.TestCase):

    def test_needs_service(self):
        tire = OctoprimeTires(0.5, 0.9, 0.9, 0.9)
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()