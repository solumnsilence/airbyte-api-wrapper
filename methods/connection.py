import logging

from exceptions import (InvalidInputResponseError,
                        NotFoundResponseError,
                        AirbyteConnectionError)
from objects.connection import (ConnectionCreate,
                                ConnectionRead,
                                ConnectionUpdate,
                                ConnectionReadList,
                                ConnectionIdRequestBody)
from objects.general import ConnectionState
from objects.scheduler import JobInfoRead
from objects.workspace import WorkspaceIdRequestBody
from utils import perform_request


def create_connection(connection_create: ConnectionCreate):
    """
    Create a connection between a source and a destination
    """

    response = perform_request(path='/v1/connections/create', data=connection_create.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return ConnectionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def update_connection(connection_update: ConnectionUpdate):
    """
    Update a connection
    """

    response = perform_request(path='/v1/connections/update', data=connection_update.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return ConnectionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_connections_for_workspace(workspace_id_request_body: WorkspaceIdRequestBody):
    """
    Returns all connections for a workspace.
    """

    response = perform_request(path='/v1/connections/list', data=workspace_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return ConnectionReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_connection(connection_id_request_body: ConnectionIdRequestBody):
    """
    Get a connection
    """

    response = perform_request(path='/v1/connections/get', data=connection_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return ConnectionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_state(connection_id_request_body: ConnectionIdRequestBody):
    """
    Fetch the current state for a connection.
    """

    response = perform_request(path='/v1/state/get', data=connection_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return ConnectionState.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def delete_connection(connection_id_request_body: ConnectionIdRequestBody):
    """
    Delete a connection
    """

    response = perform_request(path='/v1/connections/delete', data=connection_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 204:
        logging.info('The resource was deleted successfully.')
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def sync_connection(connection_id_request_body: ConnectionIdRequestBody):
    """
    Trigger a manual sync of the connection
    """

    response = perform_request(path='/v1/connections/sync', data=connection_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return JobInfoRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def reset_connection(connection_id_request_body: ConnectionIdRequestBody):
    """
    Reset the data for the connection. Deletes data generated by the connection in the destination. Resets any cursors back to initial state.
    """

    response = perform_request(path='/v1/connections/reset', data=connection_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return JobInfoRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
