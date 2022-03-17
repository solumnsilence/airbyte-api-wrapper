from exceptions import (NotFoundResponseError,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.workspace import (Notification,
                               NotificationRead)
from utils import perform_request


def try_notification_config(notification: Notification):
    """
    Try sending a notifications
    """

    response = perform_request(path='/v1/notifications/try', data=notification.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return NotificationRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
