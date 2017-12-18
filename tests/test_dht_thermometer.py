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
		
	def test_get_reading(self):
		thermometer = DhtThermometer('Thermometer 1', 4)
		
		formatted_measurement = thermometer.get_formatted_measurement((26.7, 33.4))
		self.assertIsInstance(formatted_measurement, str)
		self.assertEqual(formatted_measurement, "Temp=26.7*  Humidity=33.4%")
		
	def test_get_reading_no_values_throws_exception(self):
		thermometer = DhtThermometer('Thermometer 1', 4)
		
		self.assertRaises(ValueError, thermometer.get_formatted_measurement, (26.7,))

if __name__ == '__main__':
	unittest.main()
