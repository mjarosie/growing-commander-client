import sys
from datetime import timedelta
from dht_thermometer import DhtThermometer

import Adafruit_DHT
from measurement_reader import MeasurementReader

def run():
	# mr = MeasurementReader(timedelta(seconds=10), 2)
	temperature_source = DhtThermometer('Thermometer 1', 4)
	(humidity, temperature) = temperature_source.get_reading()
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
	else:
		print('Failed to get reading. Try again!')

if __name__ == '__main__':
	run()
