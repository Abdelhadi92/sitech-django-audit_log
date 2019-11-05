from django.db.models.signals import post_save, post_delete
from sitech_audit_log import AuditLogManager


post_save.connect(AuditLogManager._post_save)
post_delete.connect(AuditLogManager._post_delete)


