from typing import List

from dict_digger import dig

from utils import Object


class CheckOperationRead(Object):
    """
    Attributes
    ----------
    status : str
        Could be one of ['succeeded', 'failed'] values.
    message : str

    """

    def __init__(self, status: str, message: str = None):
        self.status = status
        self.message = message

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'status': dig(data, 'status'),
                'message': dig(data, 'message')
            })


class OperatorDbt(Object):
    """
    Attributes
    ----------
    git_repo_url : str

    git_repo_branch : str

    docker_image : str

    dbt_arguments : str

    """

    def __init__(self, git_repo_url: str, git_repo_branch: str = None, docker_image: str = None,
                 dbt_arguments: str = None):
        self.git_repo_url = git_repo_url
        self.git_repo_branch = git_repo_branch
        self.docker_image = docker_image
        self.dbt_arguments = dbt_arguments

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'git_repo_url': dig(data, 'gitRepoUrl'),
                'git_repo_branch': dig(data, 'gitRepoBranch'),
                'docker_image': dig(data, 'dockerImage'),
                'dbt_arguments': dig(data, 'dbtArguments')
            })


class OperatorNormalization(Object):
    """
    Attributes
    ----------
    option : str
        Could be one of ['basic'] values.
    """

    def __init__(self, option: str = None):
        self.option = option

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'option': dig(data, 'option')
            })


class OperatorConfiguration(Object):
    """
    Attributes
    ----------
    operator_type : str
        Could be one of ['normalization', 'dbt'] values.
    normalization : OperatorNormalization

    dbt : OperatorDbt

    """

    def __init__(self, operator_type: str, normalization: OperatorNormalization = None, dbt: OperatorDbt = None):
        self.operator_type = operator_type
        self.normalization = normalization
        self.dbt = dbt

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'operator_type': dig(data, 'operatorType'),
                'normalization': OperatorNormalization.from_data(dig(data, 'normalization')),
                'dbt': OperatorDbt.from_data(dig(data, 'dbt'))
            })


class OperationRead(Object):
    """
    Attributes
    ----------
    workspace_id : str
        Should be in 'uuid' format.
    operation_id : str
        Should be in 'uuid' format.
    name : str

    operator_configuration : OperatorConfiguration

    """

    def __init__(self, workspace_id: str, operation_id: str, name: str, operator_configuration: OperatorConfiguration):
        self.workspace_id = workspace_id
        self.operation_id = operation_id
        self.name = name
        self.operator_configuration = operator_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'workspace_id': dig(data, 'workspaceId'),
                'operation_id': dig(data, 'operationId'),
                'name': dig(data, 'name'),
                'operator_configuration': OperatorConfiguration.from_data(dig(data, 'operatorConfiguration'))
            })


class OperationReadList(Object):
    """
    Attributes
    ----------
    operations : List[OperationRead]

    """

    def __init__(self, operations: List[OperationRead]):
        self.operations = operations

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'operations': [OperationRead.from_data(item) for item in dig(data, 'operations')]
            })


class WebBackendOperationCreateOrUpdate(Object):
    """
    Attributes
    ----------
    operation_id : str
        Should be in 'uuid' format.
    workspace_id : str
        Should be in 'uuid' format.
    name : str

    operator_configuration : OperatorConfiguration

    """

    def __init__(self, workspace_id: str, name: str, operator_configuration: OperatorConfiguration,
                 operation_id: str = None):
        self.operation_id = operation_id
        self.workspace_id = workspace_id
        self.name = name
        self.operator_configuration = operator_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'operation_id': dig(data, 'operationId'),
                'workspace_id': dig(data, 'workspaceId'),
                'name': dig(data, 'name'),
                'operator_configuration': OperatorConfiguration.from_data(dig(data, 'operatorConfiguration'))
            })


class OperationUpdate(Object):
    """
    Attributes
    ----------
    operation_id : str
        Should be in 'uuid' format.
    name : str

    operator_configuration : OperatorConfiguration

    """

    def __init__(self, operation_id: str, name: str, operator_configuration: OperatorConfiguration):
        self.operation_id = operation_id
        self.name = name
        self.operator_configuration = operator_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'operation_id': dig(data, 'operationId'),
                'name': dig(data, 'name'),
                'operator_configuration': OperatorConfiguration.from_data(dig(data, 'operatorConfiguration'))
            })


class OperationCreate(Object):
    """
    Attributes
    ----------
    workspace_id : str
        Should be in 'uuid' format.
    name : str

    operator_configuration : OperatorConfiguration

    """

    def __init__(self, workspace_id: str, name: str, operator_configuration: OperatorConfiguration):
        self.workspace_id = workspace_id
        self.name = name
        self.operator_configuration = operator_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'workspace_id': dig(data, 'workspaceId'),
                'name': dig(data, 'name'),
                'operator_configuration': OperatorConfiguration.from_data(dig(data, 'operatorConfiguration'))
            })


class OperationIdRequestBody(Object):
    """
    Attributes
    ----------
    operation_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, operation_id: str):
        self.operation_id = operation_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'operation_id': dig(data, 'OperationId')
            })
