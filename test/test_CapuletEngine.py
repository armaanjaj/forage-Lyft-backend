import unittest
from engine.CapuletEngine import CapuletEngine

class testCapuletEngine(unittest.TestCase):

    def test_needs_service(self):
        engine = CapuletEngine(60000, 20000)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()