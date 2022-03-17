from exceptions import (NotFoundResponseError,
                        AirbyteConnectionError)
from objects.web_backend import (AirbyteArchive,
                                 ImportRead,
                                 UploadRead,
                                 ImportRequestBody)
from objects.workspace import WorkspaceIdRequestBody
from utils import perform_request


def export_archive():
    """
    Export Airbyte Configuration and Data Archive
    """

    response = perform_request(path='/v1/deployment/export', type='post', content_type='application/post')
    if response.status_code == 200:
        return AirbyteArchive.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def import_archive(airbyte_archive: AirbyteArchive):
    """
    Import Airbyte Configuration and Data Archive
    """

    response = perform_request(path='/v1/deployment/import', data=airbyte_archive.to_data(), type='post',
                               content_type='application/x-gzip')
    if response.status_code == 200:
        return ImportRead.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def export_workspace(workspace_id_request_body: WorkspaceIdRequestBody):
    """
    Export Airbyte Workspace Configuration
    """

    response = perform_request(path='/v1/deployment/export_workspace', data=workspace_id_request_body.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return AirbyteArchive.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def upload_archive_resource(airbyte_archive: AirbyteArchive):
    """
    Upload a GZIP archive tarball and stage it in the server's cache as a temporary resource
    """

    response = perform_request(path='/v1/deployment/upload_archive_resource', data=airbyte_archive.to_data(),
                               type='post', content_type='application/x-gzip')
    if response.status_code == 200:
        return UploadRead.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def import_into_workspace(import_request_body: ImportRequestBody):
    """
    Import Airbyte Configuration into Workspace (this operation might change ids of imported configurations). Note, in order to use this api endpoint, you might need to upload a temporary archive resource with 'deployment/upload_archive_resource' first

    """

    response = perform_request(path='/v1/deployment/import_into_workspace', data=import_request_body.to_data(),
                               type='post', content_type='application/json')
    if response.status_code == 200:
        return ImportRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
