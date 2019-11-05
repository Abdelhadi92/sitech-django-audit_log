from django.apps import AppConfig


class AuditLogConfig(AppConfig):
    name = 'sitech_audit_log'

    def ready(self):
        import sitech_audit_log.signals
