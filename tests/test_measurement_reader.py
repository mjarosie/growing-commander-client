from source.measurement_reader import MeasurementReader, get_results_aggregate
from source.measurement_source import MeasurementSource
import unittest
from mock import MagicMock
from datetime import datetime, timedelta
import pandas as pd


class TestMeasureReader(unittest.TestCase):

	def test_init(self):
		mr = MeasurementReader(timedelta(seconds=60), timedelta(seconds=10), 1)
		self.assertEqual(mr.idle_time, timedelta(seconds=60))
		self.assertEqual(mr.duration, timedelta(seconds=10))
		self.assertEqual(mr.number_of_measurements, 1)
		
	def test_add_source(self):
		mr = MeasurementReader(timedelta(seconds=10), timedelta(seconds=10), 1)
		new_source = MeasurementSource("Device 1", '*C')
		mr.add_source(new_source)
		self.assertEqual(len(mr.sources), 1)
		self.assertIs(mr.sources["Device 1"], new_source)
		self.assertEqual(mr.sources["Device 1"].device_unique_name, "Device 1")
		
	def test_get_measurements(self):
		mr = MeasurementReader(timedelta(seconds=10), timedelta(seconds=10), 1)
		
		device_name = "Device 1"
		data = [['Device 1', 'temperature', '*C', 26.6], ['Device 1', 'humidity', '%', 33.3]]
		measurement_to_be_returned = pd.DataFrame(data, columns=['device_name', 'measurement_type', 'measurement_unit', 'measurement_value'])
		
		# Create and mock the measurements device.
		new_source = MeasurementSource(device_name)
		new_source.get_measurement = MagicMock(return_value=measurement_to_be_returned)
		
		mr.add_source(new_source)
		
		res = mr.get_measurements()
		
		self.assertEqual(res.shape, (2, 4))
		self.assertEqual(0, cmp(res.columns.tolist(), ['device_name', 'measurement_type', 'measurement_unit', 'measurement_value']))

	def test_get_results_aggregate(self):
		timestamp1 = datetime(2017, 12, 20, 21, 30, 10)
		timestamp2 = datetime(2017, 12, 20, 21, 30, 20)
		timestamp3 = datetime(2017, 12, 20, 21, 30, 50)
		
		data = [
			[timestamp1, 'Device 1', 'temperature', '*C', 20.0],
			[timestamp1, 'Device 1', 'humidity', '%', 30.0],
			
			[timestamp2, 'Device 1', 'temperature', '*C', 22.0],
			[timestamp2, 'Device 1', 'humidity', '%', 35.0],
			
			[timestamp3, 'Device 1', 'temperature', '*C', 25.0],
			[timestamp3, 'Device 1', 'humidity', '%', 40.0],
			
			[timestamp1, 'Device 2', 'temperature', '*C', 30.0],
			[timestamp1, 'Device 2', 'humidity', '%', 50.0],
			
			[timestamp2, 'Device 2', 'temperature', '*C', 32.0],
			[timestamp2, 'Device 2', 'humidity', '%', 55.0],
			
			[timestamp3, 'Device 2', 'temperature', '*C', 35.0],
			[timestamp3, 'Device 2', 'humidity', '%', 60.0]
			]
		df = pd.DataFrame(data, columns=['timestamp', 'device_name', 'measurement_type', 'measurement_unit', 'measurement_value'])
		res = get_results_aggregate(df)
		
		self.assertEqual(res.shape, (4, 5))
		
if __name__ == '__main__':
	unittest.main()
