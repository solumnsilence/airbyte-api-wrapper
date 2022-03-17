from exceptions import (InvalidInputResponseError,
                        NotFoundResponseError,
                        AirbyteConnectionError)
from objects.destination_definition import (DestinationDefinitionCreate,
                                            DestinationDefinitionRead,
                                            DestinationDefinitionUpdate,
                                            DestinationDefinitionReadList,
                                            DestinationDefinitionIdRequestBody)
from utils import perform_request


def create_destination_definition(destination_definition_create: DestinationDefinitionCreate):
    """
    Creates a destinationsDefinition
    """

    response = perform_request(path='/v1/destination_definitions/create', data=destination_definition_create.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return DestinationDefinitionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def update_destination_definition(destination_definition_update: DestinationDefinitionUpdate):
    """
    Update destinationDefinition
    """

    response = perform_request(path='/v1/destination_definitions/update', data=destination_definition_update.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return DestinationDefinitionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_destination_definitions():
    """
    List all the destinationDefinitions the current Airbyte deployment is configured to use
    """

    response = perform_request(path='/v1/destination_definitions/list', type='post', content_type='application/post')
    if response.status_code == 200:
        return DestinationDefinitionReadList.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def list_latest_destination_definitions():
    """
    List the latest destinationDefinitions Airbyte supports
    """

    response = perform_request(path='/v1/destination_definitions/list_latest', type='post',
                               content_type='application/post')
    if response.status_code == 200:
        return DestinationDefinitionReadList.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_destination_definition(destination_definition_id_request_body: DestinationDefinitionIdRequestBody):
    """
    Get destinationDefinition
    """

    response = perform_request(path='/v1/destination_definitions/get',
                               data=destination_definition_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DestinationDefinitionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
