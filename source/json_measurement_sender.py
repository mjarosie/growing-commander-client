import requests

from measurement_sender import MeasurementSender
from source import get_logger


class JsonMeasurementSender(MeasurementSender):
    def __init__(self, login, password, server_protocol, server_address, server_port, api_version):
        self.login = login
        self.password = password
        self.server_protocol = server_protocol
        self.server_address = server_address
        self.server_port = server_port
        self.api_version = api_version

        self.log = get_logger(__name__)

        self.authentication_token = None

        self.base_api_url = '{}://{}:{}/api/{}'.format(self.server_protocol, self.server_address, self.server_port,
                                                       self.api_version)

    def get_auth_token(self):
        payload = {
            'name': self.login,
            'password': self.password
        }
        url = self.base_api_url + '/auth/login'
        self.log.info('Sending request for auth token to %s', url)

        response = None
        try:
            response = requests.post(url, json=payload).json()
        except requests.exceptions.InvalidSchema as ex:
            self.log.error('get_auth_token response error. %s', str(ex))
        except requests.exceptions.ConnectionError as ex:
            self.log.error('get_auth_token ConnectionError while trying to send a request. %s', str(ex))

        if response is None:
            self.log.info('Could not obtain the meaningful response from the server')
            return None

        if response['status'] != 'success':
            self.log.error('Could not obtain the authentication token: %s', response['message'])
            return None
        elif 'auth_token' in response:
            self.log.info('Successfully obtained authentication token!')
            return response['auth_token']
        else:
            self.log.error('Incorrect response from the server while obtaining authentication token.')
            return None

    def send(self, raw_data):
        data = raw_data.to_json(orient='index', force_ascii=False, date_format='iso')

        if self.authentication_token is None:
            self.authentication_token = self.get_auth_token()

        url = self.base_api_url + '/measurement'

        self.log.info('Sending results to the given endpoint: %s', url)

        payload = {
            'auth_token': self.authentication_token,
            'data': data
        }

        response = requests.post(url, json=payload)
        if len(response.content) == 0:
            raise RuntimeError('Incorrect server response')
        response = response.json()

        if response['status'] != 'success':
            self.log.debug('Authentication token is expired or invalid. Trying to obtain a new one...')
            # Authentication token is expired or invalid. Try to obtain a new one.
            self.authentication_token = self.get_auth_token()

            self.log.info('Sending request for auth token to %s', url)
            response = requests.post(url, json=payload).json()

            if response['status'] != 'success':
                raise RuntimeError('Unable to send results to the server')

        # If we're here - sending data was a success.
        self.log.info('Successfully sent measurement results to server!')
