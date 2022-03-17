import logging

from exceptions import (NotFoundResponseError,
                        ExceptionResponse,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.oauth import (SetInstancewideSourceOauthParamsRequestBody,
                           SourceOauthConsentRequest,
                           OAuthConsentRead,
                           CompleteSourceOauthRequest,
                           CompleteOauthResponse,
                           DestinationOauthConsentRequest,
                           CompleteDestinationOAuthRequest,
                           SetInstancewideDestinationOauthParamsRequestBody)
from utils import perform_request


def set_instancewide_source_oauth_params(
        set_instancewide_source_oauth_params_request_body: SetInstancewideSourceOauthParamsRequestBody):
    """
    Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.

    """

    response = perform_request(path='/v1/source_oauths/oauth_params/create',
                               data=set_instancewide_source_oauth_params_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        logging.info('Successful')
    elif response.status_code == 400:
        raise ExceptionResponse(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_source_o_auth_consent(source_oauth_consent_request: SourceOauthConsentRequest):
    """
    Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.
    """

    response = perform_request(path='/v1/source_oauths/get_consent_url', data=source_oauth_consent_request.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return OAuthConsentRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def complete_source_o_auth(complete_source_oauth_request: CompleteSourceOauthRequest):
    """
    Given a source def ID generate an access/refresh token etc.
    """

    response = perform_request(path='/v1/source_oauths/complete_oauth', data=complete_source_oauth_request.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return CompleteOauthResponse.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_destination_o_auth_consent(destination_oauth_consent_request: DestinationOauthConsentRequest):
    """
    Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.
    """

    response = perform_request(path='/v1/destination_oauths/get_consent_url',
                               data=destination_oauth_consent_request.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return OAuthConsentRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def complete_destination_o_auth(complete_destination_o_auth_request: CompleteDestinationOAuthRequest):
    """
    Given a destination def ID generate an access/refresh token etc.
    """

    response = perform_request(path='/v1/destination_oauths/complete_oauth',
                               data=complete_destination_o_auth_request.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return CompleteOauthResponse.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def set_instancewide_destination_oauth_params(
        set_instancewide_destination_oauth_params_request_body: SetInstancewideDestinationOauthParamsRequestBody):
    """
    Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.

    """

    response = perform_request(path='/v1/destination_oauths/oauth_params/create',
                               data=set_instancewide_destination_oauth_params_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        logging.info('Successful')
    elif response.status_code == 400:
        raise ExceptionResponse(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
