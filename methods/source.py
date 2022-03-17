import logging

from exceptions import (InvalidInputResponseError,
                        NotFoundResponseError,
                        AirbyteConnectionError)
from objects.general import CheckConnectionRead
from objects.source import (SourceCreate,
                            SourceRead,
                            SourceUpdate,
                            SourceReadList,
                            SourceIdRequestBody,
                            SourceDiscoverSchemaRead)
from objects.workspace import WorkspaceIdRequestBody
from utils import perform_request


def create_source(source_create: SourceCreate):
    """
    Create a source
    """

    response = perform_request(path='/v1/sources/create', data=source_create.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return SourceRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def update_source(source_update: SourceUpdate):
    """
    Update a source
    """

    response = perform_request(path='/v1/sources/update', data=source_update.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return SourceRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_sources_for_workspace(workspace_id_request_body: WorkspaceIdRequestBody):
    """
    List sources for workspace
    """

    response = perform_request(path='/v1/sources/list', data=workspace_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return SourceReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_source(source_id_request_body: SourceIdRequestBody):
    """
    Get source
    """

    response = perform_request(path='/v1/sources/get', data=source_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return SourceRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def delete_source(source_id_request_body: SourceIdRequestBody):
    """
    Delete a source
    """

    response = perform_request(path='/v1/sources/delete', data=source_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 204:
        logging.info('The resource was deleted successfully.')
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def check_connection_to_source(source_id_request_body: SourceIdRequestBody):
    """
    Check connection to the source
    """

    response = perform_request(path='/v1/sources/check_connection', data=source_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return CheckConnectionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def check_connection_to_source_for_update(source_update: SourceUpdate):
    """
    Check connection for a proposed update to a source
    """

    response = perform_request(path='/v1/sources/check_connection_for_update', data=source_update.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return CheckConnectionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def discover_schema_for_source(source_id_request_body: SourceIdRequestBody):
    """
    Discover the schema catalog of the source
    """

    response = perform_request(path='/v1/sources/discover_schema', data=source_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return SourceDiscoverSchemaRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
