from dict_digger import dig

from utils import Object


class HealthCheckRead(Object):
    """
    Attributes
    ----------
    db : bool

    """

    def __init__(self, db: bool):
        self.db = db

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'db': dig(data, 'db')
            })
