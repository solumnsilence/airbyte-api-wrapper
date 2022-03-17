import logging

from exceptions import (InvalidInputResponseError,
                        NotFoundResponseError,
                        AirbyteConnectionError)
from objects.connection import ConnectionIdRequestBody
from objects.operations import (OperatorConfiguration,
                                CheckOperationRead,
                                OperationCreate,
                                OperationRead,
                                OperationUpdate,
                                OperationReadList,
                                OperationIdRequestBody)
from utils import perform_request


def check_operation(operator_configuration: OperatorConfiguration):
    """
    Check if an operation to be created is valid
    """

    response = perform_request(path='/v1/operations/check', data=operator_configuration.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return CheckOperationRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def create_operation(operation_create: OperationCreate):
    """
    Create an operation to be applied as part of a connection pipeline
    """

    response = perform_request(path='/v1/operations/create', data=operation_create.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return OperationRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def update_operation(operation_update: OperationUpdate):
    """
    Update an operation
    """

    response = perform_request(path='/v1/operations/update', data=operation_update.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return OperationRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_operations_for_connection(connection_id_request_body: ConnectionIdRequestBody):
    """
    Returns all operations for a connection.
    """

    response = perform_request(path='/v1/operations/list', data=connection_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return OperationReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_operation(operation_id_request_body: OperationIdRequestBody):
    """
    Returns an operation
    """

    response = perform_request(path='/v1/operations/get', data=operation_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return OperationRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def delete_operation(operation_id_request_body: OperationIdRequestBody):
    """
    Delete an operation
    """

    response = perform_request(path='/v1/operations/delete', data=operation_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 204:
        logging.info('The resource was deleted successfully.')
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
