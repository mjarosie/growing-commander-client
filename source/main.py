import sys
from datetime import timedelta
from dht_thermometer import DhtThermometer

import Adafruit_DHT
from measurement_reader import MeasurementReader

def run():
	mr = MeasurementReader(timedelta(seconds=10), 2)
	temperature_source = DhtThermometer('Thermometer 1', 4)
	mr.add_source(temperature_source)
	
	mr.start_to_measure()

if __name__ == '__main__':
	run()
