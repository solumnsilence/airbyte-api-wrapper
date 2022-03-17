from exceptions import AirbyteConnectionError
from objects.health import HealthCheckRead
from utils import perform_request


def get_health_check():
    """
    Health Check
    """

    response = perform_request(path='/v1/health', type='get', content_type='application/post')
    if response.status_code == 200:
        return HealthCheckRead.from_data(data=response.json())
    else:
        raise AirbyteConnectionError(response)
