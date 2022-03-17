from exceptions import (NotFoundResponseError,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.connection import (WebBackendConnectionRequestBody,
                                WebBackendConnectionCreate,
                                WebBackendConnectionUpdate,
                                WebBackendConnectionSearch)
from objects.destination import (DestinationCreate,
                                 DestinationRead)
from objects.source import (SourceCreate,
                            SourceRead)
from objects.web_backend import (WebBackendConnectionReadList,
                                 WebBackendConnectionRead)
from objects.workspace import WorkspaceIdRequestBody
from utils import perform_request


def web_backend_list_connections_for_workspace(workspace_id_request_body: WorkspaceIdRequestBody):
    """
    Returns all connections for a workspace.
    """

    response = perform_request(path='/v1/web_backend/connections/list', data=workspace_id_request_body.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return WebBackendConnectionReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def web_backend_get_connection(web_backend_connection_request_body: WebBackendConnectionRequestBody):
    """
    Get a connection
    """

    response = perform_request(path='/v1/web_backend/connections/get',
                               data=web_backend_connection_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return WebBackendConnectionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def web_backend_create_connection(web_backend_connection_create: WebBackendConnectionCreate):
    """
    Create a connection
    """

    response = perform_request(path='/v1/web_backend/connections/create', data=web_backend_connection_create.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return WebBackendConnectionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def web_backend_update_connection(web_backend_connection_update: WebBackendConnectionUpdate):
    """
    Update a connection
    """

    response = perform_request(path='/v1/web_backend/connections/update', data=web_backend_connection_update.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return WebBackendConnectionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def web_backend_connection_search(web_backend_connection_search: WebBackendConnectionSearch):
    """
    Search connections
    """

    response = perform_request(path='/v1/web_backend/connections/search', data=web_backend_connection_search.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return WebBackendConnectionReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def web_backend_create_source(source_create: SourceCreate):
    """
    Create a source
    """

    response = perform_request(path='/v1/web_backend/sources/create', data=source_create.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return SourceRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def web_backend_create_destination(destination_create: DestinationCreate):
    """
    Create a destination
    """

    response = perform_request(path='/v1/web_backend/destinations/create', data=destination_create.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return DestinationRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
