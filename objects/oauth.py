from dict_digger import dig

from utils import Object


class SetInstancewideDestinationOauthParamsRequestBody(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    params : dict

    """

    def __init__(self, destination_definition_id: str, params: dict):
        self.destination_definition_id = destination_definition_id
        self.params = params

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'params': dig(data, 'params')
            })


class SetInstancewideSourceOauthParamsRequestBody(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    params : dict

    """

    def __init__(self, source_definition_id: str, params: dict):
        self.source_definition_id = source_definition_id
        self.params = params

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'params': dig(data, 'params')
            })


class CompleteOauthResponse(Object):
    """
    """


class CompleteDestinationOAuthRequest(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    redirect_url : str
        When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.
    query_params : dict
        The query parameters present in the redirect URL after a user granted consent e.g auth code.
    """

    def __init__(self, destination_definition_id: str, workspace_id: str, redirect_url: str = None,
                 query_params: dict = None):
        self.destination_definition_id = destination_definition_id
        self.workspace_id = workspace_id
        self.redirect_url = redirect_url
        self.query_params = query_params

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'workspace_id': dig(data, 'workspaceId'),
                'redirect_url': dig(data, 'redirectUrl'),
                'query_params': dig(data, 'queryParams')
            })


class CompleteSourceOauthRequest(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    redirect_url : str
        When completing OAuth flow to gain an access token, some API sometimes requires to verify that the app re-send the redirectUrl that was used when consent was given.
    query_params : dict
        The query parameters present in the redirect URL after a user granted consent e.g auth code.
    """

    def __init__(self, source_definition_id: str, workspace_id: str, redirect_url: str = None,
                 query_params: dict = None):
        self.source_definition_id = source_definition_id
        self.workspace_id = workspace_id
        self.redirect_url = redirect_url
        self.query_params = query_params

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'workspace_id': dig(data, 'workspaceId'),
                'redirect_url': dig(data, 'redirectUrl'),
                'query_params': dig(data, 'queryParams')
            })


class OAuthConsentRead(Object):
    """
    Attributes
    ----------
    consent_url : str

    """

    def __init__(self, consent_url: str):
        self.consent_url = consent_url

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'consent_url': dig(data, 'consentUrl')
            })


class DestinationOauthConsentRequest(Object):
    """
    Attributes
    ----------
    destination_definition_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    redirect_url : str
        The url to redirect to after getting the user consent.
    """

    def __init__(self, destination_definition_id: str, workspace_id: str, redirect_url: str):
        self.destination_definition_id = destination_definition_id
        self.workspace_id = workspace_id
        self.redirect_url = redirect_url

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'destination_definition_id': dig(data, 'destinationDefinitionId'),
                'workspace_id': dig(data, 'workspaceId'),
                'redirect_url': dig(data, 'redirectUrl')
            })


class SourceOauthConsentRequest(Object):
    """
    Attributes
    ----------
    source_definition_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    redirect_url : str
        The url to redirect to after getting the user consent.
    """

    def __init__(self, source_definition_id: str, workspace_id: str, redirect_url: str):
        self.source_definition_id = source_definition_id
        self.workspace_id = workspace_id
        self.redirect_url = redirect_url

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'source_definition_id': dig(data, 'sourceDefinitionId'),
                'workspace_id': dig(data, 'workspaceId'),
                'redirect_url': dig(data, 'redirectUrl')
            })
