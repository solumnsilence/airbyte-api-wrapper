from typing import List

from dict_digger import dig

from utils import Object


class SourceDefinitionRead(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    name : str

    docker_repository : str

    docker_image_tag : str

    documentation_url : str
        Should be in 'uri' format.
    icon : str

    """

    def __init__(self, source_definition_id: str, name: str, docker_repository: str, docker_image_tag: str,
                 documentation_url: str = None, icon: str = None):
        self.source_definition_id = source_definition_id
        self.name = name
        self.docker_repository = docker_repository
        self.docker_image_tag = docker_image_tag
        self.documentation_url = documentation_url
        self.icon = icon

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'name': dig(data, 'name'),
                'docker_repository': dig(data, 'dockerRepository'),
                'docker_image_tag': dig(data, 'dockerImageTag'),
                'documentation_url': dig(data, 'documentationUrl'),
                'icon': dig(data, 'icon')
            })


class SourceDefinitionReadList(Object):
    """
    Attributes
    ----------
    source_definitions : List[SourceDefinitionRead]

    """

    def __init__(self, source_definitions: List[SourceDefinitionRead]):
        self.source_definitions = source_definitions

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definitions': [SourceDefinitionRead.from_data(item) for item in dig(data, 'sourceDefinitions')]
            })


class SourceDefinitionUpdate(Object):
    """
    Update the SourceDefinition. Currently, the only allowed attribute to update is the default docker image version.

    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    docker_image_tag : str

    """

    def __init__(self, source_definition_id: str, docker_image_tag: str):
        self.source_definition_id = source_definition_id
        self.docker_image_tag = docker_image_tag

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'docker_image_tag': dig(data, 'dockerImageTag')
            })


class SourceDefinitionCreate(Object):
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


class SourceDefinitionIdRequestBody(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, source_definition_id: str):
        self.source_definition_id = source_definition_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId')
            })
