from dict_digger import dig

from utils import Object


class SlugRequestBody(Object):
    """
    Attributes
    ----------
    slug : str

    """

    def __init__(self, slug: str):
        self.slug = slug

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'slug': dig(data, 'slug')
            })
