default_app_config = 'sitech_audit_log.apps.AuditLogConfig'
from django.conf import settings
from django.utils.module_loading import import_string
from django.utils import timezone


class AuditLogMixin:
    log_operations = ['deleted', 'created', 'updated']
    ignore_changed_fields = []

class AuditLogManager:

    @classmethod
    def save(cls, audit_log, storages=None):
        if not isinstance(audit_log, AuditLog):
            raise Exception("The audit_log should be instance of AuditLog")

        if not storages:
            storages = getattr(settings, 'AUDIT_LOG_STORAGES', ['sitech_audit_log.backends.database.DatabaseBackend'])
        if not storages:
            return False

        for storage_path in storages:
            storage = import_string(storage_path)
            storage().save(audit_log)
        return  True


class AuditLog:
    __slots__ = ['auditable', 'operation', 'values', 'creator', 'creator_ip', 'creator_agent', 'created_at']

    # Create a new AuditLog instance.
    def __init__(self, auditable=None, operation=None, values=None, creator=None, creator_ip=None, creator_agent=None, created_at=None):
        self.auditable = auditable
        self.operation = operation
        self.values = [] if values is None else values
        self.creator = creator
        self.creator_ip = creator_ip
        self.creator_agent = creator_agent
        self.created_at = timezone.now() if created_at is None else created_at

    # Set the log auditable.
    def set_auditable(self, auditable):
        self.auditable = auditable
        return self

    # Set the log operation.
    def set_operation(self, operation):
        self.operation = operation
        return self

    # Set the log values.
    def set_values(self, values):
        self.values = values
        return self

    # Set the log creator.
    def set_creator(self, creator):
        self.creator = creator
        return self

    # Set the log creator_ip.
    def set_creator_ip(self, creator_ip):
        self.creator_ip = creator_ip
        return self

    # Set the log creator_agent.
    def set_creator_agent(self, creator_agent):
        self.creator_agent = creator_agent
        return self

    # Set the log created_at.
    def set_created_at(self, created_at):
        self.created_at = created_at
        return self

    # Set the log created_at.
    def save(self, storages=None):
        AuditLogManager.save(self)
