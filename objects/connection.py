from typing import List

from dict_digger import dig

from objects.destination import DestinationSearch
from objects.general import ResourceRequirements
from objects.operations import (OperationCreate,
                                WebBackendOperationCreateOrUpdate)
from objects.schema_catalog import AirbyteCatalog
from objects.source import SourceSearch
from utils import Object


class ConnectionSchedule(Object):
    """
    if null, then no schedule is set.

    Attributes
    ----------
    units : int
        Should be in 'int64' format.
    time_unit : str
        Could be one of ['minutes', 'hours', 'days', 'weeks', 'months'] values.
    """

    def __init__(self, units: int, time_unit: str):
        self.units = units
        self.time_unit = time_unit

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'units': dig(data, 'units'),
                'time_unit': dig(data, 'timeUnit')
            })


class ConnectionRead(Object):
    """
    Attributes
    ----------
    connection_id : str
        Should be in 'uuid' format.
    name : str

    namespace_definition : str
        Method used for computing final namespace in destination. Could be one of ['source', 'destination', 'customformat'] values.
    namespace_format : str
        Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'. For example ${SOURCE_NAMESPACE}.
    prefix : str
        Prefix that will be prepended to the name of each stream when it is written to the destination.
    source_id : str
        Should be in 'uuid' format.
    destination_id : str
        Should be in 'uuid' format.
    operation_ids : List[str]

    sync_catalog : AirbyteCatalog
        describes the available schema (catalog).
    schedule : ConnectionSchedule
        if null, then no schedule is set.
    status : str
        Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. Could be one of ['active', 'inactive', 'deprecated'] values.
    resource_requirements : ResourceRequirements
        optional resource requirements to run workers (blank for unbounded allocations).
    """

    def __init__(self, connection_id: str, name: str, source_id: str, destination_id: str, sync_catalog: AirbyteCatalog,
                 status: str, namespace_definition: str = 'source', namespace_format: str = None, prefix: str = None,
                 operation_ids: List[str] = None, schedule: ConnectionSchedule = None,
                 resource_requirements: ResourceRequirements = None):
        self.connection_id = connection_id
        self.name = name
        self.namespace_definition = namespace_definition
        self.namespace_format = namespace_format
        self.prefix = prefix
        self.source_id = source_id
        self.destination_id = destination_id
        self.operation_ids = operation_ids
        self.sync_catalog = sync_catalog
        self.schedule = schedule
        self.status = status
        self.resource_requirements = resource_requirements

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connection_id': dig(data, 'connectionId'),
                'name': dig(data, 'name'),
                'namespace_definition': dig(data, 'namespaceDefinition'),
                'namespace_format': dig(data, 'namespaceFormat'),
                'prefix': dig(data, 'prefix'),
                'source_id': dig(data, 'sourceId'),
                'destination_id': dig(data, 'destinationId'),
                'operation_ids': [dig(item) for item in dig(data, 'operationIds')] if dig(data,
                                                                                          'operationIds') else None,
                'sync_catalog': AirbyteCatalog.from_data(dig(data, 'syncCatalog')),
                'schedule': ConnectionSchedule.from_data(dig(data, 'schedule')),
                'status': dig(data, 'status'),
                'resource_requirements': ResourceRequirements.from_data(dig(data, 'resourceRequirements'))
            })


class ConnectionReadList(Object):
    """
    Attributes
    ----------
    connections : List[ConnectionRead]

    """

    def __init__(self, connections: List[ConnectionRead]):
        self.connections = connections

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connections': [ConnectionRead.from_data(item) for item in dig(data, 'connections')]
            })


class WebBackendConnectionSearch(Object):
    """
    Attributes
    ----------
    connection_id : str
        Should be in 'uuid' format.
    name : str

    namespace_definition : str
        Method used for computing final namespace in destination. Could be one of ['source', 'destination', 'customformat'] values.
    namespace_format : str
        Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'. For example ${SOURCE_NAMESPACE}.
    prefix : str
        Prefix that will be prepended to the name of each stream when it is written to the destination.
    source_id : str
        Should be in 'uuid' format.
    destination_id : str
        Should be in 'uuid' format.
    schedule : ConnectionSchedule
        if null, then no schedule is set.
    status : str
        Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. Could be one of ['active', 'inactive', 'deprecated'] values.
    source : SourceSearch

    destination : DestinationSearch

    """

    def __init__(self, connection_id: str = None, name: str = None, namespace_definition: str = 'source',
                 namespace_format: str = None, prefix: str = None, source_id: str = None, destination_id: str = None,
                 schedule: ConnectionSchedule = None, status: str = None, source: SourceSearch = None,
                 destination: DestinationSearch = None):
        self.connection_id = connection_id
        self.name = name
        self.namespace_definition = namespace_definition
        self.namespace_format = namespace_format
        self.prefix = prefix
        self.source_id = source_id
        self.destination_id = destination_id
        self.schedule = schedule
        self.status = status
        self.source = source
        self.destination = destination

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connection_id': dig(data, 'connectionId'),
                'name': dig(data, 'name'),
                'namespace_definition': dig(data, 'namespaceDefinition'),
                'namespace_format': dig(data, 'namespaceFormat'),
                'prefix': dig(data, 'prefix'),
                'source_id': dig(data, 'sourceId'),
                'destination_id': dig(data, 'destinationId'),
                'schedule': ConnectionSchedule.from_data(dig(data, 'schedule')),
                'status': dig(data, 'status'),
                'source': SourceSearch.from_data(dig(data, 'source')),
                'destination': DestinationSearch.from_data(dig(data, 'destination'))
            })


class WebBackendConnectionUpdate(Object):
    """
    Attributes
    ----------
    connection_id : str
        Should be in 'uuid' format.
    namespace_definition : str
        Method used for computing final namespace in destination. Could be one of ['source', 'destination', 'customformat'] values.
    namespace_format : str
        Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'. For example ${SOURCE_NAMESPACE}.
    prefix : str
        Prefix that will be prepended to the name of each stream when it is written to the destination.
    operation_ids : List[str]

    sync_catalog : AirbyteCatalog
        describes the available schema (catalog).
    schedule : ConnectionSchedule
        if null, then no schedule is set.
    status : str
        Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. Could be one of ['active', 'inactive', 'deprecated'] values.
    resource_requirements : ResourceRequirements
        optional resource requirements to run workers (blank for unbounded allocations).
    with_refreshed_catalog : bool

    operations : List[WebBackendOperationCreateOrUpdate]

    """

    def __init__(self, connection_id: str, sync_catalog: AirbyteCatalog, status: str,
                 namespace_definition: str = 'source', namespace_format: str = None, prefix: str = None,
                 operation_ids: List[str] = None, schedule: ConnectionSchedule = None,
                 resource_requirements: ResourceRequirements = None, with_refreshed_catalog: bool = None,
                 operations: List[WebBackendOperationCreateOrUpdate] = None):
        self.connection_id = connection_id
        self.namespace_definition = namespace_definition
        self.namespace_format = namespace_format
        self.prefix = prefix
        self.operation_ids = operation_ids
        self.sync_catalog = sync_catalog
        self.schedule = schedule
        self.status = status
        self.resource_requirements = resource_requirements
        self.with_refreshed_catalog = with_refreshed_catalog
        self.operations = operations

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connection_id': dig(data, 'connectionId'),
                'namespace_definition': dig(data, 'namespaceDefinition'),
                'namespace_format': dig(data, 'namespaceFormat'),
                'prefix': dig(data, 'prefix'),
                'operation_ids': [dig(item) for item in dig(data, 'operationIds')] if dig(data,
                                                                                          'operationIds') else None,
                'sync_catalog': AirbyteCatalog.from_data(dig(data, 'syncCatalog')),
                'schedule': ConnectionSchedule.from_data(dig(data, 'schedule')),
                'status': dig(data, 'status'),
                'resource_requirements': ResourceRequirements.from_data(dig(data, 'resourceRequirements')),
                'with_refreshed_catalog': dig(data, 'withRefreshedCatalog'),
                'operations': [WebBackendOperationCreateOrUpdate.from_data(item) for item in
                               dig(data, 'operations')] if dig(data, 'operations') else None,
            })


class ConnectionUpdate(Object):
    """
    Attributes
    ----------
    connection_id : str
        Should be in 'uuid' format.
    namespace_definition : str
        Method used for computing final namespace in destination. Could be one of ['source', 'destination', 'customformat'] values.
    namespace_format : str
        Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'. For example ${SOURCE_NAMESPACE}.
    prefix : str
        Prefix that will be prepended to the name of each stream when it is written to the destination.
    operation_ids : List[str]

    sync_catalog : AirbyteCatalog
        describes the available schema (catalog).
    schedule : ConnectionSchedule
        if null, then no schedule is set.
    status : str
        Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. Could be one of ['active', 'inactive', 'deprecated'] values.
    resource_requirements : ResourceRequirements
        optional resource requirements to run workers (blank for unbounded allocations).
    """

    def __init__(self, connection_id: str, sync_catalog: AirbyteCatalog, status: str,
                 namespace_definition: str = 'source', namespace_format: str = None, prefix: str = None,
                 operation_ids: List[str] = None, schedule: ConnectionSchedule = None,
                 resource_requirements: ResourceRequirements = None):
        self.connection_id = connection_id
        self.namespace_definition = namespace_definition
        self.namespace_format = namespace_format
        self.prefix = prefix
        self.operation_ids = operation_ids
        self.sync_catalog = sync_catalog
        self.schedule = schedule
        self.status = status
        self.resource_requirements = resource_requirements

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connection_id': dig(data, 'connectionId'),
                'namespace_definition': dig(data, 'namespaceDefinition'),
                'namespace_format': dig(data, 'namespaceFormat'),
                'prefix': dig(data, 'prefix'),
                'operation_ids': [dig(item) for item in dig(data, 'operationIds')] if dig(data,
                                                                                          'operationIds') else None,
                'sync_catalog': AirbyteCatalog.from_data(dig(data, 'syncCatalog')),
                'schedule': ConnectionSchedule.from_data(dig(data, 'schedule')),
                'status': dig(data, 'status'),
                'resource_requirements': ResourceRequirements.from_data(dig(data, 'resourceRequirements'))
            })


class WebBackendConnectionCreate(Object):
    """
    Attributes
    ----------
    name : str
        Optional name of the connection.
    namespace_definition : str
        Method used for computing final namespace in destination. Could be one of ['source', 'destination', 'customformat'] values.
    namespace_format : str
        Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'. For example ${SOURCE_NAMESPACE}.
    prefix : str
        Prefix that will be prepended to the name of each stream when it is written to the destination.
    source_id : str
        Should be in 'uuid' format.
    destination_id : str
        Should be in 'uuid' format.
    operation_ids : List[str]

    sync_catalog : AirbyteCatalog
        describes the available schema (catalog).
    schedule : ConnectionSchedule
        if null, then no schedule is set.
    status : str
        Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. Could be one of ['active', 'inactive', 'deprecated'] values.
    resource_requirements : ResourceRequirements
        optional resource requirements to run workers (blank for unbounded allocations).
    operations : List[OperationCreate]

    """

    def __init__(self, source_id: str, destination_id: str, status: str, name: str = None,
                 namespace_definition: str = 'source', namespace_format: str = None, prefix: str = None,
                 operation_ids: List[str] = None, sync_catalog: AirbyteCatalog = None,
                 schedule: ConnectionSchedule = None, resource_requirements: ResourceRequirements = None,
                 operations: List[OperationCreate] = None):
        self.name = name
        self.namespace_definition = namespace_definition
        self.namespace_format = namespace_format
        self.prefix = prefix
        self.source_id = source_id
        self.destination_id = destination_id
        self.operation_ids = operation_ids
        self.sync_catalog = sync_catalog
        self.schedule = schedule
        self.status = status
        self.resource_requirements = resource_requirements
        self.operations = operations

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'name': dig(data, 'name'),
                'namespace_definition': dig(data, 'namespaceDefinition'),
                'namespace_format': dig(data, 'namespaceFormat'),
                'prefix': dig(data, 'prefix'),
                'source_id': dig(data, 'sourceId'),
                'destination_id': dig(data, 'destinationId'),
                'operation_ids': [dig(item) for item in dig(data, 'operationIds')] if dig(data,
                                                                                          'operationIds') else None,
                'sync_catalog': AirbyteCatalog.from_data(dig(data, 'syncCatalog')),
                'schedule': ConnectionSchedule.from_data(dig(data, 'schedule')),
                'status': dig(data, 'status'),
                'resource_requirements': ResourceRequirements.from_data(dig(data, 'resourceRequirements')),
                'operations': [OperationCreate.from_data(item) for item in dig(data, 'operations')] if dig(data,
                                                                                                           'operations') else None,
            })


class ConnectionCreate(Object):
    """
    Attributes
    ----------
    name : str
        Optional name of the connection.
    namespace_definition : str
        Method used for computing final namespace in destination. Could be one of ['source', 'destination', 'customformat'] values.
    namespace_format : str
        Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'. For example ${SOURCE_NAMESPACE}.
    prefix : str
        Prefix that will be prepended to the name of each stream when it is written to the destination.
    source_id : str
        Should be in 'uuid' format.
    destination_id : str
        Should be in 'uuid' format.
    operation_ids : List[str]

    sync_catalog : AirbyteCatalog
        describes the available schema (catalog).
    schedule : ConnectionSchedule
        if null, then no schedule is set.
    status : str
        Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. Could be one of ['active', 'inactive', 'deprecated'] values.
    resource_requirements : ResourceRequirements
        optional resource requirements to run workers (blank for unbounded allocations).
    """

    def __init__(self, source_id: str, destination_id: str, status: str, name: str = None,
                 namespace_definition: str = 'source', namespace_format: str = None, prefix: str = None,
                 operation_ids: List[str] = None, sync_catalog: AirbyteCatalog = None,
                 schedule: ConnectionSchedule = None, resource_requirements: ResourceRequirements = None):
        self.name = name
        self.namespace_definition = namespace_definition
        self.namespace_format = namespace_format
        self.prefix = prefix
        self.source_id = source_id
        self.destination_id = destination_id
        self.operation_ids = operation_ids
        self.sync_catalog = sync_catalog
        self.schedule = schedule
        self.status = status
        self.resource_requirements = resource_requirements

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'name': dig(data, 'name'),
                'namespace_definition': dig(data, 'namespaceDefinition'),
                'namespace_format': dig(data, 'namespaceFormat'),
                'prefix': dig(data, 'prefix'),
                'source_id': dig(data, 'sourceId'),
                'destination_id': dig(data, 'destinationId'),
                'operation_ids': [dig(item) for item in dig(data, 'operationIds')] if dig(data,
                                                                                          'operationIds') else None,
                'sync_catalog': AirbyteCatalog.from_data(dig(data, 'syncCatalog')),
                'schedule': ConnectionSchedule.from_data(dig(data, 'schedule')),
                'status': dig(data, 'status'),
                'resource_requirements': ResourceRequirements.from_data(dig(data, 'resourceRequirements'))
            })


class WebBackendConnectionRequestBody(Object):
    """
    Attributes
    ----------
    with_refreshed_catalog : bool

    connection_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, connection_id: str, with_refreshed_catalog: bool = None):
        self.with_refreshed_catalog = with_refreshed_catalog
        self.connection_id = connection_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'with_refreshed_catalog': dig(data, 'withRefreshedCatalog'),
                'connection_id': dig(data, 'connectionId')
            })


class DbMigrationRequestBody(Object):
    """
    Attributes
    ----------
    database : str

    """

    def __init__(self, database: str):
        self.database = database

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'database': dig(data, 'database')
            })


class ConnectionIdRequestBody(Object):
    """
    Attributes
    ----------
    connection_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, connection_id: str):
        self.connection_id = connection_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connection_id': dig(data, 'connectionId')
            })
