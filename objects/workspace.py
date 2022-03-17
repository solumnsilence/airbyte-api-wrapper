from typing import List

from dict_digger import dig

from utils import Object


class SlackNotificationConfiguration(Object):
    """
    Attributes
    ----------
    webhook : str

    """

    def __init__(self, webhook: str):
        self.webhook = webhook

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'webhook': dig(data, 'webhook')
            })


class Notification(Object):
    """
    Attributes
    ----------
    notification_type : str
        Could be one of ['slack'] values.
    send_on_success : bool

    send_on_failure : bool

    slack_configuration : SlackNotificationConfiguration

    """

    def __init__(self, notification_type: str, send_on_success: bool, send_on_failure: bool,
                 slack_configuration: SlackNotificationConfiguration = None):
        self.notification_type = notification_type
        self.send_on_success = send_on_success
        self.send_on_failure = send_on_failure
        self.slack_configuration = slack_configuration

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'notification_type': dig(data, 'notificationType'),
                'send_on_success': dig(data, 'sendOnSuccess'),
                'send_on_failure': dig(data, 'sendOnFailure'),
                'slack_configuration': SlackNotificationConfiguration.from_data(dig(data, 'slackConfiguration'))
            })


class WorkspaceUpdate(Object):
    """
    Attributes
    ----------
    workspace_id : str
        Should be in 'uuid' format.
    email : str
        Should be in 'email' format.
    initial_setup_complete : bool

    display_setup_wizard : bool

    anonymous_data_collection : bool

    news : bool

    security_updates : bool

    notifications : List[Notification]

    """

    def __init__(self, workspace_id: str, initial_setup_complete: bool, anonymous_data_collection: bool, news: bool,
                 security_updates: bool, email: str = None, display_setup_wizard: bool = None,
                 notifications: List[Notification] = None):
        self.workspace_id = workspace_id
        self.email = email
        self.initial_setup_complete = initial_setup_complete
        self.display_setup_wizard = display_setup_wizard
        self.anonymous_data_collection = anonymous_data_collection
        self.news = news
        self.security_updates = security_updates
        self.notifications = notifications

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'workspace_id': dig(data, 'workspaceId'),
                'email': dig(data, 'email'),
                'initial_setup_complete': dig(data, 'initialSetupComplete'),
                'display_setup_wizard': dig(data, 'displaySetupWizard'),
                'anonymous_data_collection': dig(data, 'anonymousDataCollection'),
                'news': dig(data, 'news'),
                'security_updates': dig(data, 'securityUpdates'),
                'notifications': [Notification.from_data(item) for item in dig(data, 'notifications')] if dig(data,
                                                                                                              'notifications') else None,
            })


class WorkspaceRead(Object):
    """
    Attributes
    ----------
    workspace_id : str
        Should be in 'uuid' format.
    customer_id : str
        Should be in 'uuid' format.
    email : str
        Should be in 'email' format.
    name : str

    slug : str

    initial_setup_complete : bool

    display_setup_wizard : bool

    anonymous_data_collection : bool

    news : bool

    security_updates : bool

    notifications : List[Notification]

    """

    def __init__(self, workspace_id: str, customer_id: str, name: str, slug: str, initial_setup_complete: bool,
                 email: str = None, display_setup_wizard: bool = None, anonymous_data_collection: bool = None,
                 news: bool = None, security_updates: bool = None, notifications: List[Notification] = None):
        self.workspace_id = workspace_id
        self.customer_id = customer_id
        self.email = email
        self.name = name
        self.slug = slug
        self.initial_setup_complete = initial_setup_complete
        self.display_setup_wizard = display_setup_wizard
        self.anonymous_data_collection = anonymous_data_collection
        self.news = news
        self.security_updates = security_updates
        self.notifications = notifications

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'workspace_id': dig(data, 'workspaceId'),
                'customer_id': dig(data, 'customerId'),
                'email': dig(data, 'email'),
                'name': dig(data, 'name'),
                'slug': dig(data, 'slug'),
                'initial_setup_complete': dig(data, 'initialSetupComplete'),
                'display_setup_wizard': dig(data, 'displaySetupWizard'),
                'anonymous_data_collection': dig(data, 'anonymousDataCollection'),
                'news': dig(data, 'news'),
                'security_updates': dig(data, 'securityUpdates'),
                'notifications': [Notification.from_data(item) for item in dig(data, 'notifications')] if dig(data,
                                                                                                              'notifications') else None,
            })


class WorkspaceReadList(Object):
    """
    Attributes
    ----------
    workspaces : List[WorkspaceRead]

    """

    def __init__(self, workspaces: List[WorkspaceRead]):
        self.workspaces = workspaces

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'workspaces': [WorkspaceRead.from_data(item) for item in dig(data, 'workspaces')]
            })


class WorkspaceIdRequestBody(Object):
    """
    Attributes
    ----------
    workspace_id : str
        Should be in 'uuid' format.
    """

    def __init__(self, workspace_id: str):
        self.workspace_id = workspace_id

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'workspace_id': dig(data, 'workspaceId')
            })


class NotificationRead(Object):
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


class WorkspaceCreate(Object):
    """
    Attributes
    ----------
    email : str
        Should be in 'email' format.
    anonymous_data_collection : bool

    name : str

    news : bool

    security_updates : bool

    notifications : List[Notification]

    display_setup_wizard : bool

    """

    def __init__(self, name: str, email: str = None, anonymous_data_collection: bool = None, news: bool = None,
                 security_updates: bool = None, notifications: List[Notification] = None,
                 display_setup_wizard: bool = None):
        self.email = email
        self.anonymous_data_collection = anonymous_data_collection
        self.name = name
        self.news = news
        self.security_updates = security_updates
        self.notifications = notifications
        self.display_setup_wizard = display_setup_wizard

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'email': dig(data, 'email'),
                'anonymous_data_collection': dig(data, 'anonymousDataCollection'),
                'name': dig(data, 'name'),
                'news': dig(data, 'news'),
                'security_updates': dig(data, 'securityUpdates'),
                'notifications': [Notification.from_data(item) for item in dig(data, 'notifications')] if dig(data,
                                                                                                              'notifications') else None,
                'display_setup_wizard': dig(data, 'displaySetupWizard')
            })
