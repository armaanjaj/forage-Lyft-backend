import unittest
from engine.SternmanEngine import SternmanEngine

class testSternmanEngine(unittest.TestCase):

    def test_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()