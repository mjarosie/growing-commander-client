from source.measurement_reader import MeasurementReader
from source.measurement_source import MeasurementSource
import unittest
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

if __name__ == '__main__':
	unittest.main()
