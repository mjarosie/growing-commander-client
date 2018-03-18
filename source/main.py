import configparser
from datetime import timedelta

from dht_thermometer import DhtThermometer
from json_measurement_sender import JsonMeasurementSender
from measurement_reader import MeasurementReader
from source import get_logger


def check_config(config):
    if len(config.sections()) == 0:
        logger = get_logger(__name__)
        logger.error('Config file not found.')
        return False

    if 'measurement-server' not in config or 'measurements' not in config:
        logger = get_logger(__name__)
        logger.error('Provided configuration is not correct.')
        return False

    return True


def run():
    config = configparser.ConfigParser()

    # Previous config data is overwritten with the data from consecutive files,
    # so the more important the file is, the further down the list it is.
    config.read(['config.ini.example', 'config.ini'])

    if not check_config(config):
        exit(1)

    server_config = config['measurement-server']

    sender = None
    try:
        sender = JsonMeasurementSender(server_config['login'], server_config['password'], server_config['protocol'],
                                       server_config['address'], server_config['port'], server_config['api_version'])
        logger = get_logger(__name__)
        logger.info('Created a JSON measurement sender')
    except KeyError:
        logger = get_logger(__name__)
        logger.error('Error while creating a measurement sender.')
        exit(1)

    measurements_config = config['measurements']

    try:
        measurement_idle_time = timedelta(seconds=int(measurements_config['measurement_idle_time']))
        measurement_duration = timedelta(seconds=int(measurements_config['measurement_duration']))
    except TypeError as e:
        logger = get_logger(__name__)
        logger.error('Incorrect measurement timings. %s', str(e))

        logger.info('Using default values for measurement timings')
        # Filling in with default values.
        measurement_idle_time = timedelta(seconds=60)
        measurement_duration = timedelta(seconds=10)

    mr = MeasurementReader(measurement_idle_time, measurement_duration, 2, sender)

    temperature_source = DhtThermometer('Thermometer 1', 4)
    mr.add_source(temperature_source)

    mr.start_to_measure()


if __name__ == '__main__':
    run()
