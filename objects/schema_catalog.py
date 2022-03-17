from typing import List

from dict_digger import dig

from utils import Object


class AirbyteStreamConfiguration(Object):
    """
    the mutable part of the stream to configure the destination

    Attributes
    ----------
    sync_mode : str
        Could be one of ['full_refresh', 'incremental'] values.
    cursor_field : List[str]
        Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental`. Otherwise it is ignored.
    destination_sync_mode : str
        Could be one of ['append', 'overwrite', 'append_dedup'] values.
    primary_key : List[List[str]]
        Paths to the fields that will be used as primary key. This field is REQUIRED if `destination_sync_mode` is `*_dedup`. Otherwise it is ignored.
    alias_name : str
        Alias name to the stream to be used in the destination.
    selected : bool

    """

    def __init__(self, sync_mode: str, destination_sync_mode: str, cursor_field: List[str] = None,
                 primary_key: List[List[str]] = None, alias_name: str = None, selected: bool = None):
        self.sync_mode = sync_mode
        self.cursor_field = cursor_field
        self.destination_sync_mode = destination_sync_mode
        self.primary_key = primary_key
        self.alias_name = alias_name
        self.selected = selected

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'sync_mode': dig(data, 'syncMode'),
                'cursor_field': [dig(item) for item in dig(data, 'cursorField')] if dig(data, 'cursorField') else None,
                'destination_sync_mode': dig(data, 'destinationSyncMode'),
                'primary_key': data['primaryKey'],
                'alias_name': dig(data, 'aliasName'),
                'selected': dig(data, 'selected')
            })


class AirbyteStream(Object):
    """
    the immutable schema defined by the source

    Attributes
    ----------
    name : str
        Stream's name.
    json_schema : dict

    supported_sync_modes : List[str]

    source_defined_cursor : bool
        If the source defines the cursor field, then any other cursor field inputs will be ignored. If it does not, either the user_provided one is used, or the default one is used as a backup.
    default_cursor_field : List[str]
        Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves.
    source_defined_primary_key : List[List[str]]
        If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves.
    namespace : str
        Optional Source-defined namespace. Airbyte streams from the same sources should have the same namespace. Currently only used by JDBC destinations to determine what schema to write to.
    """

    def __init__(self, name: str, json_schema: dict = None, supported_sync_modes: List[str] = None,
                 source_defined_cursor: bool = None, default_cursor_field: List[str] = None,
                 source_defined_primary_key: List[List[str]] = None, namespace: str = None):
        self.name = name
        self.json_schema = json_schema
        self.supported_sync_modes = supported_sync_modes
        self.source_defined_cursor = source_defined_cursor
        self.default_cursor_field = default_cursor_field
        self.source_defined_primary_key = source_defined_primary_key
        self.namespace = namespace

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'name': dig(data, 'name'),
                'json_schema': dig(data, 'jsonSchema'),
                'supported_sync_modes': [dig(item) for item in dig(data, 'supportedSyncModes')] if dig(data,
                                                                                                       'supportedSyncModes') else None,
                'source_defined_cursor': dig(data, 'sourceDefinedCursor'),
                'default_cursor_field': [dig(item) for item in dig(data, 'defaultCursorField')] if dig(data,
                                                                                                       'defaultCursorField') else None,
                'source_defined_primary_key': data['sourceDefinedPrimaryKey'],
                'namespace': dig(data, 'namespace')
            })


class AirbyteStreamAndConfiguration(Object):
    """
    each stream is split in two parts; the immutable schema from source and mutable configuration for destination

    Attributes
    ----------
    stream : AirbyteStream
        the immutable schema defined by the source.
    config : AirbyteStreamConfiguration
        the mutable part of the stream to configure the destination.
    """

    def __init__(self, stream: AirbyteStream = None, config: AirbyteStreamConfiguration = None):
        self.stream = stream
        self.config = config

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'stream': AirbyteStream.from_data(dig(data, 'stream')),
                'config': AirbyteStreamConfiguration.from_data(dig(data, 'config'))
            })


class AirbyteCatalog(Object):
    """
    describes the available schema (catalog).

    Attributes
    ----------
    streams : List[AirbyteStreamAndConfiguration]

    """

    def __init__(self, streams: List[AirbyteStreamAndConfiguration]):
        self.streams = streams

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'streams': [AirbyteStreamAndConfiguration.from_data(item) for item in dig(data, 'streams')]
            })
