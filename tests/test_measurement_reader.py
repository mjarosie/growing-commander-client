from source.measurement_reader import MeasurementReader
from source.measurement_source import MeasurementSource
import unittest
from mock import MagicMock
from datetime import timedelta

class TestMeasureReader(unittest.TestCase):

	def test_init(self):
		mr = MeasurementReader(timedelta(seconds=10), 1)
		self.assertEqual(mr.duration, timedelta(seconds=10))
		self.assertEqual(mr.number_of_measurements, 1)
		
	def test_add_source(self):
		mr = MeasurementReader(timedelta(seconds=10), 1)
		new_source = MeasurementSource("Device 1")
		mr.add_source(new_source)
		self.assertEqual(len(mr.sources), 1)
		self.assertIs(mr.sources["Device 1"], new_source)
		self.assertEqual(mr.sources["Device 1"].device_unique_name, "Device 1")
		
	def test_get_measurements(self):
		mr = MeasurementReader(timedelta(seconds=10), 1)
		
		device_name = "Device 1"
		measurement_to_be_returned = (20.0, 30.0)
		def get_measurement_side_effect(arg):
			arg[device_name] = measurement_to_be_returned
			return arg
		
		# Create and mock the measurements device.
		new_source = MeasurementSource(device_name)
		new_source.get_measurement = MagicMock(side_effect=get_measurement_side_effect)
		
		mr.add_source(new_source)
		
		results_storage = {}
		mr.get_measurements(results_storage)
		
		self.assertEqual(len(results_storage), 1)
		self.assertEqual(results_storage[device_name], measurement_to_be_returned)
		self.assertEqual(mr.sources[device_name].device_unique_name, device_name)

if __name__ == '__main__':
	unittest.main()
