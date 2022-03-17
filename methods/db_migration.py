from exceptions import (NotFoundResponseError,
                        InvalidInputResponseError,
                        AirbyteConnectionError)
from objects.connection import DbMigrationRequestBody
from objects.db_migration import (DbMigrationReadList,
                                  DbMigrationExecutionRead)
from utils import perform_request


def list_migrations(db_migration_request_body: DbMigrationRequestBody):
    """
    List all database migrations
    """

    response = perform_request(path='/v1/db_migrations/list', data=db_migration_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DbMigrationReadList.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)


def execute_migrations(db_migration_request_body: DbMigrationRequestBody):
    """
    Migrate the database to the latest version
    """

    response = perform_request(path='/v1/db_migrations/migrate', data=db_migration_request_body.to_data(), type='post',
                               content_type='application/json')
    if response.status_code == 200:
        return DbMigrationExecutionRead.from_data(data=response.json())
    elif response.status_code == 404:
        raise NotFoundResponseError(data=response.json())
    elif response.status_code == 422:
        raise InvalidInputResponseError(data=response.json())
    else:
        raise AirbyteConnectionError(response)
