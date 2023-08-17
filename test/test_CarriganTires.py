import unittest
from tire.CarriganTires import CarriganTires

class testCarriganTires(unittest.TestCase):

    def test_needs_service(self):
        tire = CarriganTires(0.1, 0.9, 0.4, 0.5)
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()