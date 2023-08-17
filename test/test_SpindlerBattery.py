import unittest
from battery.SpindlerBattery import SplinderBattery
from datetime import date

class testSpindlerBattery(unittest.TestCase):

    def test_needs_service(self):
        battery = SplinderBattery(date.fromisoformat("2020-03-17"), date.today())
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()