import logging

from exceptions import AirbyteConnectionError
from utils import perform_request


def get_open_api_spec():
    """
    Returns the openapi specification
    """

    response = perform_request(path='/v1/openapi', type='get', content_type='application/post')
    if response.status_code == 200:
        logging.info('Returns the openapi specification file')
    else:
        raise AirbyteConnectionError(response)
