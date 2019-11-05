default_app_config = 'audit_log.apps.AuditLoggingConfig'


class LoggingMixin:
    ignore_changed_fields = []
    log_only_dirty_fields = True


class LoggingManager:

    @classmethod
    def post_save(cls, sender, instance, **kwargs):
        if isinstance(instance, LoggingMixin):
            print('post_save ==', sender)

    @classmethod
    def post_delete(cls, sender, instance, **kwargs):
        if isinstance(instance, LoggingMixin):
            print('post_delete ==', sender)

    @classmethod
    def save(cls, **kwargs):
        pass




