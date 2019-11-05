from django.db.models.signals import post_save, post_delete
from sitech_audit_log import LoggingManager


post_save.connect(LoggingManager.post_save)
post_delete.connect(LoggingManager.post_delete)


