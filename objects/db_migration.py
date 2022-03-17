from typing import List

from dict_digger import dig

from utils import Object


class DbMigrationRead(Object):
    """
    Attributes
    ----------
    migration_type : str

    migration_version : str

    migration_description : str

    migration_state : str
        Could be one of ['pending', 'above_target', 'below_baseline', 'baseline', 'ignored', 'missing_success', 'missing_failed', 'success', 'undone', 'available', 'failed', 'out_of_order', 'future_success', 'future_failed', 'outdated', 'superseded', 'deleted'] values.
    migrated_by : str

    migrated_at : int
        Should be in 'int64' format.
    migration_script : str

    """

    def __init__(self, migration_type: str, migration_version: str, migration_description: str,
                 migration_state: str = None, migrated_by: str = None, migrated_at: int = None,
                 migration_script: str = None):
        self.migration_type = migration_type
        self.migration_version = migration_version
        self.migration_description = migration_description
        self.migration_state = migration_state
        self.migrated_by = migrated_by
        self.migrated_at = migrated_at
        self.migration_script = migration_script

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'migration_type': dig(data, 'migrationType'),
                'migration_version': dig(data, 'migrationVersion'),
                'migration_description': dig(data, 'migrationDescription'),
                'migration_state': dig(data, 'migrationState'),
                'migrated_by': dig(data, 'migratedBy'),
                'migrated_at': dig(data, 'migratedAt'),
                'migration_script': dig(data, 'migrationScript')
            })


class DbMigrationExecutionRead(Object):
    """
    Attributes
    ----------
    initial_version : str

    target_version : str

    executed_migrations : List[DbMigrationRead]

    """

    def __init__(self, initial_version: str = None, target_version: str = None,
                 executed_migrations: List[DbMigrationRead] = None):
        self.initial_version = initial_version
        self.target_version = target_version
        self.executed_migrations = executed_migrations

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'initial_version': dig(data, 'initialVersion'),
                'target_version': dig(data, 'targetVersion'),
                'executed_migrations': [DbMigrationRead.from_data(item) for item in
                                        dig(data, 'executedMigrations')] if dig(data, 'executedMigrations') else None,
            })


class DbMigrationReadList(Object):
    """
    Attributes
    ----------
    migrations : List[DbMigrationRead]

    """

    def __init__(self, migrations: List[DbMigrationRead] = None):
        self.migrations = migrations

    @classmethod
    def from_data(cls, data: dict):
        if data:
            return cls(**{
                'migrations': [DbMigrationRead.from_data(item) for item in dig(data, 'migrations')] if dig(data,
                                                                                                           'migrations') else None,
            })
