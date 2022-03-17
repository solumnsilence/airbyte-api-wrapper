from typing import Optional

from pydantic import BaseSettings, Field

from configs.dotenv import DOTENV_FILE_PATH


class AirbyteCredentialsSchema(BaseSettings):
    host: str = Field(..., description='Postgres server host.', env='airbyte_host')
    port: Optional[int] = Field(8000, description='Postgres server port.', env='airbyte_port')
    workspace_id: str = Field(..., description='Id of the Airbyte workspace.', env='airbyte_workspace_id')

    class Config:
        env_file = DOTENV_FILE_PATH


airbyte_credentials = AirbyteCredentialsSchema()


def generate_api_url(path):
    return f'http://{airbyte_credentials.host}:{airbyte_credentials.port}/api{path}'
