from django.db.models.signals import post_save, post_delete
from sitech_audit_log import AuditLogManager, AuditLog, AuditLogMixin


def _post_save_handler(sender, instance, created, **kwargs):
    if isinstance(instance, AuditLogMixin):
        operation = "created" if created else "updated"
        if operation in instance.log_operation:
            values = _get_dirty_values(instance, operation)
            if values:
                AuditLog().set_auditable(instance).set_operation(operation).set_values(values).save()


def _post_delete_handler(sender, instance, **kwargs):
    if isinstance(instance, AuditLogMixin):
        operation = "deleted"
        if operation in instance.log_operation:
            values = _get_dirty_values(instance, operation)
            if values:
                AuditLog().set_auditable(instance).set_operation(operation).set_values(values).save()

def _get_dirty_values(instance, operation):
    values = []
    if isinstance(instance, AuditLogMixin):
        for field in instance._meta.fields:
            attname, column = field.get_attname_column()
            if operation == 'deleted' or (field.name not in instance.ignore_changed_fields and instance._old_fields[attname] != getattr(instance, attname)):
                field_value = {
                    'att': attname,
                    'value': getattr(instance, attname),
                }
                if operation == 'updated':
                    field_value['old_value'] = instance._old_fields[attname]
                values.append(field_value)
    return values

post_save.connect(_post_save_handler)
post_delete.connect(_post_delete_handler)
