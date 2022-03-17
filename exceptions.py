from objects.web_backend import (NotFoundKnownExceptionInfo,
                                 KnownExceptionInfo,
                                 InvalidInputExceptionInfo)


class AirbyteConnectionError(Exception):
    def __init__(self, response):
        self.message = f'Airbyte has refused the request with status_code={response.status_code}.'
        self.response = response
        super().__init__(self.message)


class NotFoundResponseError(Exception):
    def __init__(self, data):
        self.message = 'Object with given id was not found.'
        self.object = NotFoundKnownExceptionInfo.from_data(data=data)
        super().__init__(self.message)


class InvalidInputResponseError(Exception):
    def __init__(self, data):
        self.message = 'Input failed validation'
        self.object = InvalidInputExceptionInfo.from_data(data=data)
        super().__init__(self.message)


class ExceptionResponse(Exception):
    def __init__(self, data):
        self.message = 'Exception occurred; see message for details.'
        self.object = KnownExceptionInfo.from_data(data=data)
        super().__init__(self.message)
