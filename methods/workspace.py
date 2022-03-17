import logging

from exceptions import (InvalidInputResponseError,
                        NotFoundResponseError,
                        AirbyteConnectionError)
from objects.slug import SlugRequestBody
from objects.workspace import (WorkspaceCreate,
                               WorkspaceRead,
                               WorkspaceIdRequestBody,
                               WorkspaceReadList,
                               WorkspaceUpdate)
from utils import perform_request


def create_workspace(workspace_create: WorkspaceCreate):
    """
    Creates a workspace
    """

    response = perform_request(path='/v1/workspaces/create', data=workspace_create.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return WorkspaceRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def delete_workspace(workspace_id_request_body: WorkspaceIdRequestBody):
    """
    Deletes a workspace
    """

    response = perform_request(path='/v1/workspaces/delete', data=workspace_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 204:
        logging.info('The resource was deleted successfully.')
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_workspaces():
    """
    List all workspaces registered in the current Airbyte deployment
    """

    response = perform_request(path='/v1/workspaces/list', type='post', content_type='application/post')
    if response.status_code == 200:
        return WorkspaceReadList.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_workspace(workspace_id_request_body: WorkspaceIdRequestBody):
    """
    Find workspace by ID
    """

    response = perform_request(path='/v1/workspaces/get', data=workspace_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return WorkspaceRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_workspace_by_slug(slug_request_body: SlugRequestBody):
    """
    Find workspace by slug
    """

    response = perform_request(path='/v1/workspaces/get_by_slug', data=slug_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return WorkspaceRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def update_workspace(workspace_update: WorkspaceUpdate):
    """
    Update workspace state
    """

    response = perform_request(path='/v1/workspaces/update', data=workspace_update.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return WorkspaceRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
