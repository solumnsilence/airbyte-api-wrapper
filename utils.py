import re

import requests

from settings import generate_api_url


class InvalidRequestType(Exception):
    def __init__(self, passed_type):
        self.message = f'''Type {passed_type} is not valid request type. Please pass one of the {['post', 'get']}.'''
        super().__init__(self.message)


def to_snake_case(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()


def to_camel_case(name):
    s = ''.join(word.title() for word in name.split('_'))
    return s[:1].lower() + s[1:] if s else ''


class Object:
    def to_data(self):
        data = {}
        for k, v in self.__dict__.items():
            key = to_camel_case(k)
            if v:
                if isinstance(v, Object):
                    data[key] = v.to_data()
                elif isinstance(v, list):
                    data[key] = []
                    for item in v:
                        if isinstance(item, Object):
                            data[key].append(item.to_data())
                        else:
                            data[key].append(item)
                else:
                    data[key] = v
        return data


def perform_request(path, type, content_type, data=None):
    headers = {'Content-type': content_type}
    if type == 'post':
        return requests.post(generate_api_url(path), json=data, headers=headers)
    elif type == 'get':
        return requests.get(generate_api_url(path), json=data, headers=headers)
    else:
        raise InvalidRequestType(type)
