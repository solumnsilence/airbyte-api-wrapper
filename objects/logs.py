from typing import List

from dict_digger import dig

from utils import Object


class LogRead(Object):
    """
    Attributes
    ----------
    log_lines : List[str]

    """

    def __init__(self, log_lines: List[str]):
        self.log_lines = log_lines

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'log_lines': [dig(item) for item in dig(data, 'logLines')]
            })


class LogsRequestBody(Object):
    """
    Attributes
    ----------
    log_type : str
        type/source of logs produced. Could be one of ['server', 'scheduler'] values.
    """

    def __init__(self, log_type: str):
        self.log_type = log_type

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'log_type': dig(data, 'logType')
            })
