from typing import List

from dict_digger import dig

from objects.scheduler import SynchronousJobRead
from utils import Object


class SourceDefinitionSpecificationRead(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    documentation_url : str

    connection_specification : dict
        The specification for what values are required to configure the sourceDefinition. For example {'user': {'type': 'string'}}.
    auth_specification

    job_info : SynchronousJobRead

    """

    def __init__(self, source_definition_id: str, job_info: SynchronousJobRead, documentation_url: str = None,
                 connection_specification: dict = None, auth_specification=None):
        self.source_definition_id = source_definition_id
        self.documentation_url = documentation_url
        self.connection_specification = connection_specification
        self.auth_specification = auth_specification
        self.job_info = job_info

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'documentation_url': dig(data, 'documentationUrl'),
                'connection_specification': dig(data, 'connectionSpecification'),
                'auth_specification': dig(data, 'authSpecification'),
                'job_info': SynchronousJobRead.from_data(dig(data, 'jobInfo'))
            })


class OAuth2Specification(Object):
    """
    An object containing any metadata needed to describe this connector's Oauth flow

    Attributes
    ----------
    oauth_flow_init_parameters : List[List[str]]
        Pointers to the fields in the ConnectorSpecification which are needed to obtain the initial refresh/access tokens for the OAuth flow. Each inner array represents the path in the ConnectorSpecification of the referenced field. For example. Assume the ConnectorSpecification contains params 'app_secret', 'app_id' which are needed to get the initial refresh token. If they are not nested in the config, then the array would look like this [['app_secret'], ['app_id']] If they are nested inside, say, an object called 'auth_params' then this array would be [['auth_params', 'app_secret'], ['auth_params', 'app_id']].
    """

    def __init__(self, oauth_flow_init_parameters: List[List[str]] = None):
        self.oauth_flow_init_parameters = oauth_flow_init_parameters

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'oauth_flow_init_parameters': data['oauthFlowInitParameters']
            })


class AuthSpecification(Object):
    """
    Attributes
    ----------
    auth_type : str
        Could be one of ['oauth2.0'] values.
    oauth2_specification : OAuth2Specification
        An object containing any metadata needed to describe this connector's Oauth flow.
    """

    def __init__(self, auth_type: str = None, oauth2_specification: OAuth2Specification = None):
        self.auth_type = auth_type
        self.oauth2_specification = oauth2_specification

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'auth_type': dig(data, 'auth_type'),
                'oauth2_specification': OAuth2Specification.from_data(dig(data, 'oauth2Specification'))
            })
