from exceptions import (InvalidInputResponseError,
                        NotFoundResponseError,
                        AirbyteConnectionError)
from objects.source_definition import (SourceDefinitionCreate,
                                       SourceDefinitionRead,
                                       SourceDefinitionUpdate,
                                       SourceDefinitionReadList,
                                       SourceDefinitionIdRequestBody)
from utils import perform_request


def create_source_definition(source_definition_create: SourceDefinitionCreate):
    """
    Creates a sourceDefinition
    """

    response = perform_request(path='/v1/source_definitions/create', data=source_definition_create.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return SourceDefinitionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def update_source_definition(source_definition_update: SourceDefinitionUpdate):
    """
    Update a sourceDefinition
    """

    response = perform_request(path='/v1/source_definitions/update', data=source_definition_update.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return SourceDefinitionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_source_definitions():
    """
    List all the sourceDefinitions the current Airbyte deployment is configured to use
    """

    response = perform_request(path='/v1/source_definitions/list', type='post', content_type='application/post')
    if response.status_code == 200:
        return SourceDefinitionReadList.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_latest_source_definitions():
    """
    List the latest sourceDefinitions Airbyte supports
    """

    response = perform_request(path='/v1/source_definitions/list_latest', type='post', content_type='application/post')
    if response.status_code == 200:
        return SourceDefinitionReadList.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_source_definition(source_definition_id_request_body: SourceDefinitionIdRequestBody):
    """
    Get source
    """

    response = perform_request(path='/v1/source_definitions/get', data=source_definition_id_request_body.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return SourceDefinitionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
