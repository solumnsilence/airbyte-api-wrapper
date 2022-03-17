import logging

from exceptions import (InvalidInputResponseError,
                        NotFoundResponseError,
                        AirbyteConnectionError)
from objects.destination import (DestinationCreate,
                                 DestinationRead,
                                 DestinationUpdate,
                                 DestinationReadList,
                                 DestinationIdRequestBody)
from objects.general import CheckConnectionRead
from objects.workspace import WorkspaceIdRequestBody
from utils import perform_request


def create_destination(destination_create: DestinationCreate):
    """
    Create a destination
    """

    response = perform_request(path='/v1/destinations/create', data=destination_create.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DestinationRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def update_destination(destination_update: DestinationUpdate):
    """
    Update a destination
    """

    response = perform_request(path='/v1/destinations/update', data=destination_update.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DestinationRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_destinations_for_workspace(workspace_id_request_body: WorkspaceIdRequestBody):
    """
    List configured destinations for a workspace
    """

    response = perform_request(path='/v1/destinations/list', data=workspace_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DestinationReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_destination(destination_id_request_body: DestinationIdRequestBody):
    """
    Get configured destination
    """

    response = perform_request(path='/v1/destinations/get', data=destination_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DestinationRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def check_connection_to_destination(destination_id_request_body: DestinationIdRequestBody):
    """
    Check connection to the destination
    """

    response = perform_request(path='/v1/destinations/check_connection', data=destination_id_request_body.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return CheckConnectionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def check_connection_to_destination_for_update(destination_update: DestinationUpdate):
    """
    Check connection for a proposed update to a destination
    """

    response = perform_request(path='/v1/destinations/check_connection_for_update', data=destination_update.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return CheckConnectionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def delete_destination(destination_id_request_body: DestinationIdRequestBody):
    """
    Delete the destination
    """

    response = perform_request(path='/v1/destinations/delete', data=destination_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 204:
        logging.info('The resource was deleted successfully.')
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
