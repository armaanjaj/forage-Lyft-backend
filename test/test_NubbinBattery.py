import unittest
from battery.NubbinBattery import NubbinBattery
from datetime import date

class testNubbinBattery(unittest.TestCase):

    def test_needs_service(self):
        battery = NubbinBattery(date.fromisoformat("2018-10-21"), date.today())
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()