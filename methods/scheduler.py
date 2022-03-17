from exceptions import (InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.destination import DestinationCoreConfig
from objects.general import CheckConnectionRead
from objects.source import (SourceCoreConfig,
                            SourceDiscoverSchemaRead)
from utils import perform_request


def execute_source_check_connection(source_core_config: SourceCoreConfig):
    """
    Run check connection for a given source configuration
    """

    response = perform_request(path='/v1/scheduler/sources/check_connection', data=source_core_config.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return CheckConnectionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def execute_source_discover_schema(source_core_config: SourceCoreConfig):
    """
    Run discover schema for a given source a source configuration
    """

    response = perform_request(path='/v1/scheduler/sources/discover_schema', data=source_core_config.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return SourceDiscoverSchemaRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def execute_destination_check_connection(destination_core_config: DestinationCoreConfig):
    """
    Run check connection for a given destination configuration
    """

    response = perform_request(path='/v1/scheduler/destinations/check_connection',
                               data=destination_core_config.to_data(), type='post', content_type='application/json')
    if response.status_code == 200:
        return CheckConnectionRead.from_data(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
