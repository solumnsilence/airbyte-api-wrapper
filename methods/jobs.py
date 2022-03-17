from exceptions import (NotFoundResponseError,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.scheduler import (JobListRequestBody,
                               JobReadList,
                               JobIdRequestBody,
                               JobInfoRead)
from utils import perform_request


def list_jobs_for(job_list_request_body: JobListRequestBody):
    """
    Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.
    """

    response = perform_request(path='/v1/jobs/list', data=job_list_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return JobReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def get_job_info(job_id_request_body: JobIdRequestBody):
    """
    Get information about a job
    """

    response = perform_request(path='/v1/jobs/get', data=job_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return JobInfoRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def cancel_job(job_id_request_body: JobIdRequestBody):
    """
    Cancels a job
    """

    response = perform_request(path='/v1/jobs/cancel', data=job_id_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return JobInfoRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
