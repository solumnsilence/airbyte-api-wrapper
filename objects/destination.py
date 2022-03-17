from typing import List

from dict_digger import dig

from utils import Object


class DestinationSearch(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    destination_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the destination. The schema for this must match the schema return by destination_definition_specifications/get for the destinationDefinition. For example {'user': 'charles'}.
    name : str

    destination_name : str

    """

    def __init__(self, destination_definition_id: str = None, destination_id: str = None, workspace_id: str = None,
                 connection_configuration=None, name: str = None, destination_name: str = None):
        self.destination_definition_id = destination_definition_id
        self.destination_id = destination_id
        self.workspace_id = workspace_id
        self.connection_configuration = connection_configuration
        self.name = name
        self.destination_name = destination_name

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'destination_id': dig(data, 'destinationId'),
                'workspace_id': dig(data, 'workspaceId'),
                'connection_configuration': dig(data, 'connectionConfiguration'),
                'name': dig(data, 'name'),
                'destination_name': dig(data, 'destinationName')
            })


class DestinationRead(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    destination_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the destination. The schema for this must match the schema return by destination_definition_specifications/get for the destinationDefinition. For example {'user': 'charles'}.
    name : str

    destination_name : str

    """

    def __init__(self, destination_definition_id: str, destination_id: str, workspace_id: str, connection_configuration,
                 name: str, destination_name: str):
        self.destination_definition_id = destination_definition_id
        self.destination_id = destination_id
        self.workspace_id = workspace_id
        self.connection_configuration = connection_configuration
        self.name = name
        self.destination_name = destination_name

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'destination_id': dig(data, 'destinationId'),
                'workspace_id': dig(data, 'workspaceId'),
                'connection_configuration': dig(data, 'connectionConfiguration'),
                'name': dig(data, 'name'),
                'destination_name': dig(data, 'destinationName')
            })


class DestinationReadList(Object):
    """
    Attributes
    ----------
    destinations : List[DestinationRead]

    """

    def __init__(self, destinations: List[DestinationRead]):
        self.destinations = destinations

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destinations': [DestinationRead.from_data(item) for item in dig(data, 'destinations')]
            })


class DestinationUpdate(Object):
    """
    Attributes
    ----------
    destination_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the destination. The schema for this must match the schema return by destination_definition_specifications/get for the destinationDefinition. For example {'user': 'charles'}.
    name : str

    """

    def __init__(self, destination_id: str, connection_configuration, name: str):
        self.destination_id = destination_id
        self.connection_configuration = connection_configuration
        self.name = name

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_id': dig(data, 'destinationId'),
                'connection_configuration': dig(data, 'connectionConfiguration'),
                'name': dig(data, 'name')
            })


class DestinationCreate(Object):
    """
    Attributes
    ----------
    workspace_id : str
        Should be in 'uuid' format.
    name : str

    destination_definition_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the destination. The schema for this must match the schema return by destination_definition_specifications/get for the destinationDefinition. For example {'user': 'charles'}.
    """

    def __init__(self, workspace_id: str, name: str, destination_definition_id: str, connection_configuration):
        self.workspace_id = workspace_id
        self.name = name
        self.destination_definition_id = destination_definition_id
        self.connection_configuration = connection_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'workspace_id': dig(data, 'workspaceId'),
                'name': dig(data, 'name'),
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'connection_configuration': dig(data, 'connectionConfiguration')
            })


class DestinationCoreConfig(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the destination. The schema for this must match the schema return by destination_definition_specifications/get for the destinationDefinition. For example {'user': 'charles'}.
    """

    def __init__(self, destination_definition_id: str, connection_configuration):
        self.destination_definition_id = destination_definition_id
        self.connection_configuration = connection_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'connection_configuration': dig(data, 'connectionConfiguration')
            })


class DestinationIdRequestBody(Object):
    """
    Attributes
    ----------
    destination_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, destination_id: str):
        self.destination_id = destination_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_id': dig(data, 'destinationId')
            })
