from typing import List

from dict_digger import dig

from utils import Object


class DestinationDefinitionRead(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    name : str

    docker_repository : str

    docker_image_tag : str

    documentation_url : str
        Should be in 'uri' format.
    icon : str

    """

    def __init__(self, destination_definition_id: str, name: str, docker_repository: str, docker_image_tag: str,
                 documentation_url: str, icon: str = None):
        self.destination_definition_id = destination_definition_id
        self.name = name
        self.docker_repository = docker_repository
        self.docker_image_tag = docker_image_tag
        self.documentation_url = documentation_url
        self.icon = icon

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'name': dig(data, 'name'),
                'docker_repository': dig(data, 'dockerRepository'),
                'docker_image_tag': dig(data, 'dockerImageTag'),
                'documentation_url': dig(data, 'documentationUrl'),
                'icon': dig(data, 'icon')
            })


class DestinationDefinitionReadList(Object):
    """
    Attributes
    ----------
    destination_definitions : List[DestinationDefinitionRead]

    """

    def __init__(self, destination_definitions: List[DestinationDefinitionRead]):
        self.destination_definitions = destination_definitions

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definitions': [DestinationDefinitionRead.from_data(item) for item in
                                            dig(data, 'destinationDefinitions')]
            })


class DestinationDefinitionUpdate(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    docker_image_tag : str

    """

    def __init__(self, destination_definition_id: str, docker_image_tag: str = None):
        self.destination_definition_id = destination_definition_id
        self.docker_image_tag = docker_image_tag

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'docker_image_tag': dig(data, 'dockerImageTag')
            })


class DestinationDefinitionCreate(Object):
    """
    Attributes
    ----------
    name : str

    docker_repository : str

    docker_image_tag : str

    documentation_url : str
        Should be in 'uri' format.
    icon : str

    """

    def __init__(self, name: str, docker_repository: str, docker_image_tag: str, documentation_url: str,
                 icon: str = None):
        self.name = name
        self.docker_repository = docker_repository
        self.docker_image_tag = docker_image_tag
        self.documentation_url = documentation_url
        self.icon = icon

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'name': dig(data, 'name'),
                'docker_repository': dig(data, 'dockerRepository'),
                'docker_image_tag': dig(data, 'dockerImageTag'),
                'documentation_url': dig(data, 'documentationUrl'),
                'icon': dig(data, 'icon')
            })


class DestinationDefinitionIdRequestBody(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, destination_definition_id: str):
        self.destination_definition_id = destination_definition_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId')
            })
