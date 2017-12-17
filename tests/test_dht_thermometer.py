from source.dht_thermometer import DhtThermometer

import unittest
import Adafruit_DHT


class TestDhtThermometer(unittest.TestCase):

	def test_init(self):
		thermometer = DhtThermometer('Thermometer 1', 4)
		self.assertEqual(thermometer.gpio_pin, 4)
		self.assertEqual(thermometer.sensor_type, Adafruit_DHT.AM2302)

	def test_get_reading(self):
		'''If fails - probably the thermometer is not connected properly'''
		thermometer = DhtThermometer('Thermometer 1', 4)
		
		reading = thermometer.get_reading()
		
		self.assertIsInstance(reading[0], (int, long, float))
		self.assertIsInstance(reading[1], (int, long, float))

if __name__ == '__main__':
	unittest.main()
