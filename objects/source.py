from typing import List

from dict_digger import dig

from objects.scheduler import SynchronousJobRead
from objects.schema_catalog import AirbyteCatalog
from utils import Object


class SourceSearch(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    source_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the source. The schema for this must match the schema return by source_definition_specifications/get for the source. For example {'user': 'charles'}.
    name : str

    source_name : str

    """

    def __init__(self, source_definition_id: str = None, source_id: str = None, workspace_id: str = None,
                 connection_configuration=None, name: str = None, source_name: str = None):
        self.source_definition_id = source_definition_id
        self.source_id = source_id
        self.workspace_id = workspace_id
        self.connection_configuration = connection_configuration
        self.name = name
        self.source_name = source_name

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'source_id': dig(data, 'sourceId'),
                'workspace_id': dig(data, 'workspaceId'),
                'connection_configuration': dig(data, 'connectionConfiguration'),
                'name': dig(data, 'name'),
                'source_name': dig(data, 'sourceName')
            })


class SourceDiscoverSchemaRead(Object):
    """
    Returns the results of a discover catalog job. If the job was not successful, the catalog field will not be present. jobInfo will aways be present and its status be used to determine if the job was successful or not.

    Attributes
    ----------
    catalog : AirbyteCatalog
        describes the available schema (catalog).
    job_info : SynchronousJobRead

    """

    def __init__(self, job_info: SynchronousJobRead, catalog: AirbyteCatalog = None):
        self.catalog = catalog
        self.job_info = job_info

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'catalog': AirbyteCatalog.from_data(dig(data, 'catalog')),
                'job_info': SynchronousJobRead.from_data(dig(data, 'jobInfo'))
            })


class SourceRead(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    source_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the source. The schema for this must match the schema return by source_definition_specifications/get for the source. For example {'user': 'charles'}.
    name : str

    source_name : str

    """

    def __init__(self, source_definition_id: str, source_id: str, workspace_id: str, connection_configuration,
                 name: str, source_name: str):
        self.source_definition_id = source_definition_id
        self.source_id = source_id
        self.workspace_id = workspace_id
        self.connection_configuration = connection_configuration
        self.name = name
        self.source_name = source_name

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'source_id': dig(data, 'sourceId'),
                'workspace_id': dig(data, 'workspaceId'),
                'connection_configuration': dig(data, 'connectionConfiguration'),
                'name': dig(data, 'name'),
                'source_name': dig(data, 'sourceName')
            })


class SourceReadList(Object):
    """
    Attributes
    ----------
    sources : List[SourceRead]

    """

    def __init__(self, sources: List[SourceRead]):
        self.sources = sources

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'sources': [SourceRead.from_data(item) for item in dig(data, 'sources')]
            })


class SourceUpdate(Object):
    """
    Attributes
    ----------
    source_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the source. The schema for this must match the schema return by source_definition_specifications/get for the source. For example {'user': 'charles'}.
    name : str

    """

    def __init__(self, source_id: str, connection_configuration, name: str):
        self.source_id = source_id
        self.connection_configuration = connection_configuration
        self.name = name

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_id': dig(data, 'sourceId'),
                'connection_configuration': dig(data, 'connectionConfiguration'),
                'name': dig(data, 'name')
            })


class SourceCreate(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the source. The schema for this must match the schema return by source_definition_specifications/get for the source. For example {'user': 'charles'}.
    workspace_id : str
        Should be in 'uuid' format.
    name : str

    """

    def __init__(self, source_definition_id: str, connection_configuration, workspace_id: str, name: str):
        self.source_definition_id = source_definition_id
        self.connection_configuration = connection_configuration
        self.workspace_id = workspace_id
        self.name = name

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'connection_configuration': dig(data, 'connectionConfiguration'),
                'workspace_id': dig(data, 'workspaceId'),
                'name': dig(data, 'name')
            })


class SourceCoreConfig(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    connection_configuration
        The values required to configure the source. The schema for this must match the schema return by source_definition_specifications/get for the source. For example {'user': 'charles'}.
    """

    def __init__(self, source_definition_id: str, connection_configuration):
        self.source_definition_id = source_definition_id
        self.connection_configuration = connection_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'connection_configuration': dig(data, 'connectionConfiguration')
            })


class SourceIdRequestBody(Object):
    """
    Attributes
    ----------
    source_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, source_id: str):
        self.source_id = source_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_id': dig(data, 'sourceId')
            })
