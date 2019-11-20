"""Audit logging backend that saves logs to a database."""

from sitech_audit_log.backends.base import BaseLoggingBackend
from sitech_audit_log.models import DatabaseLogging


class DatabaseBackend(BaseLoggingBackend):

    def save(self, audit_log):
        """
        Save the given audit_log.
        """
        DatabaseLogging(
            auditable=audit_log.auditable,
            operation=audit_log.operation,
            values=audit_log.values,
            creator=audit_log.creator,
            creator_ip=audit_log.creator_ip,
            creator_agent=audit_log.creator_agent,
            created_at=audit_log.created_at,
        ).save()
