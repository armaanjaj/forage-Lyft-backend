import unittest
from engine.WilloughbyEngine import WilloughbyEngine

class testWilloughbyEngine(unittest.TestCase):

    def test_needs_service(self):
        engine = WilloughbyEngine(90000, 20000)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()