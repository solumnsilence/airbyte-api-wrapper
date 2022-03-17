from typing import List

from dict_digger import dig

from objects.connection import ConnectionSchedule
from objects.destination import DestinationRead
from objects.general import ResourceRequirements
from objects.operations import OperationRead
from objects.schema_catalog import AirbyteCatalog
from objects.source import SourceRead
from utils import Object


class InvalidInputProperty(Object):
    """
    Attributes
    ----------
    property_path : str

    invalid_value : str

    message : str

    """

    def __init__(self, property_path: str, invalid_value: str = None, message: str = None):
        self.property_path = property_path
        self.invalid_value = invalid_value
        self.message = message

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'property_path': dig(data, 'propertyPath'),
                'invalid_value': dig(data, 'invalidValue'),
                'message': dig(data, 'message')
            })


class InvalidInputExceptionInfo(Object):
    """
    Attributes
    ----------
    message : str

    exception_class_name : str

    exception_stack : List[str]

    validation_errors : List[InvalidInputProperty]

    """

    def __init__(self, message: str, validation_errors: List[InvalidInputProperty], exception_class_name: str = None,
                 exception_stack: List[str] = None):
        self.message = message
        self.exception_class_name = exception_class_name
        self.exception_stack = exception_stack
        self.validation_errors = validation_errors

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'message': dig(data, 'message'),
                'exception_class_name': dig(data, 'exceptionClassName'),
                'exception_stack': [dig(item) for item in dig(data, 'exceptionStack')] if dig(data,
                                                                                              'exceptionStack') else None,
                'validation_errors': [InvalidInputProperty.from_data(item) for item in
                                      dig(data, 'validationErrors')] if dig(data, 'validationErrors') else [],
            })


class KnownExceptionInfo(Object):
    """
    Attributes
    ----------
    message : str

    exception_class_name : str

    exception_stack : List[str]

    root_cause_exception_class_name : str

    root_cause_exception_stack : List[str]

    """

    def __init__(self, message: str, exception_class_name: str = None, exception_stack: List[str] = None,
                 root_cause_exception_class_name: str = None, root_cause_exception_stack: List[str] = None):
        self.message = message
        self.exception_class_name = exception_class_name
        self.exception_stack = exception_stack
        self.root_cause_exception_class_name = root_cause_exception_class_name
        self.root_cause_exception_stack = root_cause_exception_stack

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'message': dig(data, 'message'),
                'exception_class_name': dig(data, 'exceptionClassName'),
                'exception_stack': [dig(item) for item in dig(data, 'exceptionStack')] if dig(data,
                                                                                              'exceptionStack') else None,
                'root_cause_exception_class_name': dig(data, 'rootCauseExceptionClassName'),
                'root_cause_exception_stack': [dig(item) for item in dig(data, 'rootCauseExceptionStack')] if dig(data,
                                                                                                                  'rootCauseExceptionStack') else None,
            })


class NotFoundKnownExceptionInfo(Object):
    """
    Attributes
    ----------
    id : str

    message : str

    exception_class_name : str

    exception_stack : List[str]

    root_cause_exception_class_name : str

    root_cause_exception_stack : List[str]

    """

    def __init__(self, message: str, id: str = None, exception_class_name: str = None,
                 exception_stack: List[str] = None, root_cause_exception_class_name: str = None,
                 root_cause_exception_stack: List[str] = None):
        self.id = id
        self.message = message
        self.exception_class_name = exception_class_name
        self.exception_stack = exception_stack
        self.root_cause_exception_class_name = root_cause_exception_class_name
        self.root_cause_exception_stack = root_cause_exception_stack

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'id': dig(data, 'id'),
                'message': dig(data, 'message'),
                'exception_class_name': dig(data, 'exceptionClassName'),
                'exception_stack': [dig(item) for item in dig(data, 'exceptionStack')] if dig(data,
                                                                                              'exceptionStack') else None,
                'root_cause_exception_class_name': dig(data, 'rootCauseExceptionClassName'),
                'root_cause_exception_stack': [dig(item) for item in dig(data, 'rootCauseExceptionStack')] if dig(data,
                                                                                                                  'rootCauseExceptionStack') else None,
            })


class ImportRequestBody(Object):
    """
    Attributes
    ----------
    resource_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, resource_id: str, workspace_id: str):
        self.resource_id = resource_id
        self.workspace_id = workspace_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'resource_id': dig(data, 'resourceId'),
                'workspace_id': dig(data, 'workspaceId')
            })


class UploadRead(Object):
    """
    Attributes
    ----------
    status : str
        Could be one of ['succeeded', 'failed'] values.
    resource_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, status: str, resource_id: str = None):
        self.status = status
        self.resource_id = resource_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'status': dig(data, 'status'),
                'resource_id': dig(data, 'resourceId')
            })


class ImportRead(Object):
    """
    Attributes
    ----------
    status : str
        Could be one of ['succeeded', 'failed'] values.
    reason : str

    """

    def __init__(self, status: str, reason: str = None):
        self.status = status
        self.reason = reason

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'status': dig(data, 'status'),
                'reason': dig(data, 'reason')
            })


class AirbyteArchive(Object):
    """
    Tarball Archive (.tar.gz) of Airbyte Configuration and Database

    Attributes
    ----------
    archive : bytes

    """

    def __init__(self, archive):
        self.archive = archive

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'archive': dig(data, 'archive')
            })


class WebBackendConnectionRead(Object):
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
    sync_catalog : AirbyteCatalog
        describes the available schema (catalog).
    schedule : ConnectionSchedule
        if null, then no schedule is set.
    status : str
        Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. Could be one of ['active', 'inactive', 'deprecated'] values.
    operation_ids : List[str]

    source : SourceRead

    destination : DestinationRead

    operations : List[OperationRead]

    latest_sync_job_created_at : int
        epoch time of the latest sync job. null if no sync job has taken place. Should be in 'int64' format.
    latest_sync_job_status : str
        Could be one of ['pending', 'running', 'incomplete', 'failed', 'succeeded', 'cancelled'] values.
    is_syncing : bool

    resource_requirements : ResourceRequirements
        optional resource requirements to run workers (blank for unbounded allocations).
    """

    def __init__(self, connection_id: str, name: str, source_id: str, destination_id: str, sync_catalog: AirbyteCatalog,
                 status: str, source: SourceRead, destination: DestinationRead, is_syncing: bool,
                 namespace_definition: str = 'source', namespace_format: str = None, prefix: str = None,
                 schedule: ConnectionSchedule = None, operation_ids: List[str] = None,
                 operations: List[OperationRead] = None, latest_sync_job_created_at: int = None,
                 latest_sync_job_status: str = None, resource_requirements: ResourceRequirements = None):
        self.connection_id = connection_id
        self.name = name
        self.namespace_definition = namespace_definition
        self.namespace_format = namespace_format
        self.prefix = prefix
        self.source_id = source_id
        self.destination_id = destination_id
        self.sync_catalog = sync_catalog
        self.schedule = schedule
        self.status = status
        self.operation_ids = operation_ids
        self.source = source
        self.destination = destination
        self.operations = operations
        self.latest_sync_job_created_at = latest_sync_job_created_at
        self.latest_sync_job_status = latest_sync_job_status
        self.is_syncing = is_syncing
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
                'sync_catalog': AirbyteCatalog.from_data(dig(data, 'syncCatalog')),
                'schedule': ConnectionSchedule.from_data(dig(data, 'schedule')),
                'status': dig(data, 'status'),
                'operation_ids': [dig(item) for item in dig(data, 'operationIds')] if dig(data,
                                                                                          'operationIds') else None,
                'source': SourceRead.from_data(dig(data, 'source')),
                'destination': DestinationRead.from_data(dig(data, 'destination')),
                'operations': [OperationRead.from_data(item) for item in dig(data, 'operations')] if dig(data,
                                                                                                         'operations') else None,
                'latest_sync_job_created_at': dig(data, 'latestSyncJobCreatedAt'),
                'latest_sync_job_status': dig(data, 'latestSyncJobStatus'),
                'is_syncing': dig(data, 'isSyncing'),
                'resource_requirements': ResourceRequirements.from_data(dig(data, 'resourceRequirements'))
            })


class WebBackendConnectionReadList(Object):
    """
    Attributes
    ----------
    connections : List[WebBackendConnectionRead]

    """

    def __init__(self, connections: List[WebBackendConnectionRead]):
        self.connections = connections

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connections': [WebBackendConnectionRead.from_data(item) for item in dig(data, 'connections')]
            })
