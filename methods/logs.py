import logging

from exceptions import (NotFoundResponseError,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.logs import LogsRequestBody
from utils import perform_request


def get_logs(logs_request_body: LogsRequestBody):
    """
    Get logs
    """

    response = perform_request(path='/v1/logs/get', data=logs_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        logging.info('Returns the log file')
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
