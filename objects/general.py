from dict_digger import dig

from objects.scheduler import SynchronousJobRead
from utils import Object


class ResourceRequirements(Object):
    """
    optional resource requirements to run workers (blank for unbounded allocations)

    Attributes
    ----------
    cpu_request : str

    cpu_limit : str

    memory_request : str

    memory_limit : str

    """

    def __init__(self, cpu_request: str = None, cpu_limit: str = None, memory_request: str = None,
                 memory_limit: str = None):
        self.cpu_request = cpu_request
        self.cpu_limit = cpu_limit
        self.memory_request = memory_request
        self.memory_limit = memory_limit

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'cpu_request': dig(data, 'cpu_request'),
                'cpu_limit': dig(data, 'cpu_limit'),
                'memory_request': dig(data, 'memory_request'),
                'memory_limit': dig(data, 'memory_limit')
            })


class ConnectionState(Object):
    """
    Attributes
    ----------
    connection_id : str
        Should be in 'uuid' format.
    state : dict

    """

    def __init__(self, connection_id: str, state: dict = None):
        self.connection_id = connection_id
        self.state = state

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'connection_id': dig(data, 'connectionId'),
                'state': dig(data, 'state')
            })


class CheckConnectionRead(Object):
    """
    Attributes
    ----------
    status : str
        Could be one of ['succeeded', 'failed'] values.
    message : str

    job_info : SynchronousJobRead

    """

    def __init__(self, status: str, job_info: SynchronousJobRead, message: str = None):
        self.status = status
        self.message = message
        self.job_info = job_info

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'status': dig(data, 'status'),
                'message': dig(data, 'message'),
                'job_info': SynchronousJobRead.from_data(dig(data, 'jobInfo'))
            })
