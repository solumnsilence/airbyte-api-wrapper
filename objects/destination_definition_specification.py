from typing import List

from dict_digger import dig

from objects.scheduler import SynchronousJobRead
from utils import Object


class DestinationDefinitionSpecificationRead(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    documentation_url : str

    connection_specification
        The specification for what values are required to configure the destinationDefinition. For example {'user': {'type': 'string'}}.
    auth_specification

    job_info : SynchronousJobRead

    supported_destination_sync_modes : List[str]

    supports_dbt : bool

    supports_normalization : bool

    """

    def __init__(self, destination_definition_id: str, job_info: SynchronousJobRead, documentation_url: str = None,
                 connection_specification=None, auth_specification=None,
                 supported_destination_sync_modes: List[str] = None, supports_dbt: bool = None,
                 supports_normalization: bool = None):
        self.destination_definition_id = destination_definition_id
        self.documentation_url = documentation_url
        self.connection_specification = connection_specification
        self.auth_specification = auth_specification
        self.job_info = job_info
        self.supported_destination_sync_modes = supported_destination_sync_modes
        self.supports_dbt = supports_dbt
        self.supports_normalization = supports_normalization

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'documentation_url': dig(data, 'documentationUrl'),
                'connection_specification': dig(data, 'connectionSpecification'),
                'auth_specification': dig(data, 'authSpecification'),
                'job_info': SynchronousJobRead.from_data(dig(data, 'jobInfo')),
                'supported_destination_sync_modes': [dig(item) for item in
                                                     dig(data, 'supportedDestinationSyncModes')] if dig(data,
                                                                                                        'supportedDestinationSyncModes') else None,
                'supports_dbt': dig(data, 'supportsDbt'),
                'supports_normalization': dig(data, 'supportsNormalization')
            })
