from source.dht_thermometer import DhtThermometer
from source.utils import get_formatted_measurement
import unittest
import Adafruit_DHT
import pandas as pd
from datetime import datetime

class TestDhtThermometer(unittest.TestCase):

	def test_init(self):
		thermometer = DhtThermometer('Thermometer 1', 4)
		self.assertEqual(thermometer.gpio_pin, 4)
		self.assertEqual(thermometer.sensor_type, Adafruit_DHT.AM2302)

	def test_get_measurement(self):
		'''If fails - probably the thermometer is not connected properly'''
		thermometer = DhtThermometer('Thermometer 1', 4)
		def measure_function():
			return (25.5, 30.0)
			
		results = thermometer.get_measurement(measure_function)
		
		self.assertEqual(results['device_name'][0], 'Thermometer 1')
		self.assertEqual(results['device_name'][1], 'Thermometer 1')
		
		self.assertEqual(results['measurement_type'][0], 'humidity')
		self.assertEqual(results['measurement_type'][1], 'temperature')
		
		self.assertEqual(results['measurement_unit'][0], '%')
		self.assertEqual(results['measurement_unit'][1], '*C')
		
		self.assertEqual(results['measurement_value'][0], 25.5)
		self.assertEqual(results['measurement_value'][1], 30.0)
		
	def test_get_formated_measurement(self):
		timestamp = datetime(2017, 12, 20, 21, 30, 50)
		
		data = [timestamp, 'Device 1', 'temperature', '*C', 20.0]
		
		df = pd.Series(data, index=['timestamp', 'device_name', 'measurement_type', 'measurement_unit', 'measurement_value'])
		
		formatted_measurement = get_formatted_measurement(df)
		self.assertIsInstance(formatted_measurement, str)
		self.assertEqual(formatted_measurement, '20 Dec 2017, 21:30:50 - Device 1: temperature=20.0*C')
		
	def test_get_reading_no_values_throws_exception(self):
		self.assertRaises(TypeError, get_formatted_measurement, (26.7,))

if __name__ == '__main__':
	unittest.main()
