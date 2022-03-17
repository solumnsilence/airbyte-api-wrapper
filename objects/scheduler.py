from typing import List

from dict_digger import dig

from objects.logs import LogRead
from utils import Object


class Pagination(Object):
    """
    Attributes
    ----------
    page_size : int

    row_offset : int

    """

    def __init__(self, page_size: int = None, row_offset: int = None):
        self.page_size = page_size
        self.row_offset = row_offset

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'page_size': dig(data, 'pageSize'),
                'row_offset': dig(data, 'rowOffset')
            })


class SynchronousJobRead(Object):
    """
    Attributes
    ----------
    id : str
        Should be in 'uuid' format.
    config_type : str
        Could be one of ['check_connection_source', 'check_connection_destination', 'discover_schema', 'get_spec', 'sync', 'reset_connection'] values.
    config_id : str
        only present if a config id was provided.
    created_at : int
        Should be in 'int64' format.
    ended_at : int
        Should be in 'int64' format.
    succeeded : bool

    logs : LogRead

    """

    def __init__(self, id: str, config_type: str, created_at: int, ended_at: int, succeeded: bool,
                 config_id: str = None, logs: LogRead = None):
        self.id = id
        self.config_type = config_type
        self.config_id = config_id
        self.created_at = created_at
        self.ended_at = ended_at
        self.succeeded = succeeded
        self.logs = logs

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'id': dig(data, 'id'),
                'config_type': dig(data, 'configType'),
                'config_id': dig(data, 'configId'),
                'created_at': dig(data, 'createdAt'),
                'ended_at': dig(data, 'endedAt'),
                'succeeded': dig(data, 'succeeded'),
                'logs': LogRead.from_data(dig(data, 'logs'))
            })


class AttemptRead(Object):
    """
    Attributes
    ----------
    id : int
        Should be in 'int64' format.
    status : str
        Could be one of ['running', 'failed', 'succeeded'] values.
    created_at : int
        Should be in 'int64' format.
    updated_at : int
        Should be in 'int64' format.
    ended_at : int
        Should be in 'int64' format.
    bytes_synced : int
        Should be in 'int64' format.
    records_synced : int
        Should be in 'int64' format.
    """

    def __init__(self, id: int, status: str, created_at: int, updated_at: int, ended_at: int = None,
                 bytes_synced: int = None, records_synced: int = None):
        self.id = id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.ended_at = ended_at
        self.bytes_synced = bytes_synced
        self.records_synced = records_synced

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'id': dig(data, 'id'),
                'status': dig(data, 'status'),
                'created_at': dig(data, 'createdAt'),
                'updated_at': dig(data, 'updatedAt'),
                'ended_at': dig(data, 'endedAt'),
                'bytes_synced': dig(data, 'bytesSynced'),
                'records_synced': dig(data, 'recordsSynced')
            })


class AttemptInfoRead(Object):
    """
    Attributes
    ----------
    attempt : AttemptRead

    logs : LogRead

    """

    def __init__(self, attempt: AttemptRead, logs: LogRead):
        self.attempt = attempt
        self.logs = logs

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'attempt': AttemptRead.from_data(dig(data, 'attempt')),
                'logs': LogRead.from_data(dig(data, 'logs'))
            })


class JobRead(Object):
    """
    Attributes
    ----------
    id : int
        Should be in 'int64' format.
    config_type : str
        Could be one of ['check_connection_source', 'check_connection_destination', 'discover_schema', 'get_spec', 'sync', 'reset_connection'] values.
    config_id : str

    created_at : int
        Should be in 'int64' format.
    updated_at : int
        Should be in 'int64' format.
    status : str
        Could be one of ['pending', 'running', 'incomplete', 'failed', 'succeeded', 'cancelled'] values.
    """

    def __init__(self, id: int, config_type: str, config_id: str, created_at: int, updated_at: int, status: str):
        self.id = id
        self.config_type = config_type
        self.config_id = config_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'id': dig(data, 'id'),
                'config_type': dig(data, 'configType'),
                'config_id': dig(data, 'configId'),
                'created_at': dig(data, 'createdAt'),
                'updated_at': dig(data, 'updatedAt'),
                'status': dig(data, 'status')
            })


class JobInfoRead(Object):
    """
    Attributes
    ----------
    job : JobRead

    attempts : List[AttemptInfoRead]

    """

    def __init__(self, job: JobRead, attempts: List[AttemptInfoRead]):
        self.job = job
        self.attempts = attempts

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'job': JobRead.from_data(dig(data, 'job')),
                'attempts': [AttemptInfoRead.from_data(item) for item in dig(data, 'attempts')]
            })


class JobWithAttemptsRead(Object):
    """
    Attributes
    ----------
    job : JobRead

    attempts : List[AttemptRead]

    """

    def __init__(self, job: JobRead = None, attempts: List[AttemptRead] = None):
        self.job = job
        self.attempts = attempts

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'job': JobRead.from_data(dig(data, 'job')),
                'attempts': [AttemptRead.from_data(item) for item in dig(data, 'attempts')] if dig(data,
                                                                                                   'attempts') else None,
            })


class JobReadList(Object):
    """
    Attributes
    ----------
    jobs : List[JobWithAttemptsRead]

    """

    def __init__(self, jobs: List[JobWithAttemptsRead]):
        self.jobs = jobs

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'jobs': [JobWithAttemptsRead.from_data(item) for item in dig(data, 'jobs')]
            })


class JobIdRequestBody(Object):
    """
    Attributes
    ----------
    id : int
        Should be in 'int64' format.
    """

    def __init__(self, id: int):
        self.id = id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'id': dig(data, 'id')
            })


class JobListRequestBody(Object):
    """
    Attributes
    ----------
    config_types : List[str]

    config_id : str

    pagination : Pagination

    """

    def __init__(self, config_types: List[str], config_id: str, pagination: Pagination = None):
        self.config_types = config_types
        self.config_id = config_id
        self.pagination = pagination

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'config_types': [dig(item) for item in dig(data, 'configTypes')],
                'config_id': dig(data, 'configId'),
                'pagination': Pagination.from_data(dig(data, 'pagination'))
            })
