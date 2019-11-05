from django.db import models
from jsonfield import JSONField
from sitech_middlewares.fields import UserForeignKey


class DatabaseLogging(models.Model):
    auditable_id = models.PositiveIntegerField('Auditable Id')
    auditable_type = models.CharField(verbose_name='Auditable Type', max_length=255)
    operation = models.CharField(verbose_name='Operation', max_length=255)
    values = JSONField(verbose_name='Values')
    creator = UserForeignKey(auto_user_add=True, db_column='created_by', verbose_name="Creator")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created At')
    ip_address = models.GenericIPAddressField()
    creator_agent = models.CharField(verbose_name='Creator Agent', max_length=255)

