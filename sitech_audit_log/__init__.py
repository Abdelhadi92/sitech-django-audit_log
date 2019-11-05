default_app_config = 'sitech_audit_log.apps.AuditLogConfig'
from django.conf import settings
from django.utils.module_loading import import_string


class AuditLogMixin:
    ignore_changed_fields = []
    log_only_dirty_fields = True
    log_operation = ['deleted', 'created', 'updated']


class AuditLogManager:

    @classmethod
    def _post_save(cls, sender, instance, **kwargs):
        if isinstance(instance, AuditLogMixin):
            print('post_save ==', sender)

    @classmethod
    def _post_delete(cls, sender, instance, **kwargs):
        if isinstance(instance, AuditLogMixin):
            print('post_delete ==', sender)

    @classmethod
    def save(cls, audit_log, storages=None):
        if not isinstance(audit_log, AuditLog):
            raise Exception("The audit_log should be instance of AuditLog")

            if not storages:
                storages = getattr(settings, 'AUDIT_LOG_STORAGES', False)
            if not storages:
                return False

            for storage_path in storages:
                storage = import_string(storage_path)
                storage().save(audit_log)
            return  True


class AuditLog:
    __slots__ = ['auditable_id', 'auditable_type', 'operation', 'values', 'creator', 'creator_ip', 'creator_agent', 'created_at']

    # 
    def __init__(self, operation='', values = []):
        self.operation = operation
        self.values = values

    # 
    def set_auditable(self, auditable):
        self.auditable_type = auditable._meta.label_lower
        self.auditable_id = auditable.id
        return self
        
    # 
    def set_operation(self, operation):
        self.operation = operation
        return self

    # 
    def set_values(self, values):
        self.values = values
        return self

    # 
    def set_creator(self, creator):
        self.creator = creator
        return self

    # 
    def set_creator_ip(self, creator_ip):
        self.creator_ip = creator_ip
        return self

    #
    def set_creator_agent(self, creator_agent):
        self.creator_agent = creator_agent
        return self

    # 
    def set_created_at(self, created_at):
        self.created_at = created_at
        return self
    
    def save(self, storages=None):
        AuditLogManager.save(self)
        
