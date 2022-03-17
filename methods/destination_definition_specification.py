from exceptions import (NotFoundResponseError,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.destination_definition import DestinationDefinitionIdRequestBody
from objects.destination_definition_specification import \
    DestinationDefinitionSpecificationRead
from utils import perform_request


def get_destination_definition_specification(
        destination_definition_id_request_body: DestinationDefinitionIdRequestBody):
    """
    Get specification for a destinationDefinition
    """

    response = perform_request(path='/v1/destination_definition_specifications/get',
                               data=destination_definition_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DestinationDefinitionSpecificationRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
