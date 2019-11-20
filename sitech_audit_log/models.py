from django.db import models
from jsonfield import JSONField
from sitech_middlewares.fields import UserForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class DatabaseLogging(models.Model):
    auditable_type = models.ForeignKey(ContentType, verbose_name='Auditable Type', max_length=255, on_delete=models.CASCADE)
    auditable_id = models.PositiveIntegerField('Auditable Id')
    auditable = GenericForeignKey('auditable_type', 'auditable_id')
    operation = models.CharField(verbose_name='Operation', max_length=255)
    values = JSONField(verbose_name='Values')
    creator = UserForeignKey(auto_user_add=True, db_column='created_by', verbose_name="Creator")
    creator_ip = models.GenericIPAddressField(null=True,)
    creator_agent = models.CharField(null=True, verbose_name='Creator Agent', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created At')

