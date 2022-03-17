from exceptions import (NotFoundResponseError,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.source_definition import SourceDefinitionIdRequestBody
from objects.source_definition_specification import (
    SourceDefinitionSpecificationRead,
)
from utils import perform_request


def get_source_definition_specification(source_definition_id_request_body: SourceDefinitionIdRequestBody):
    """
    Get specification for a SourceDefinition.
    """

    response = perform_request(path='/v1/source_definition_specifications/get',
                               data=source_definition_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return SourceDefinitionSpecificationRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
