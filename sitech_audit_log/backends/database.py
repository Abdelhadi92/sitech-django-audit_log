"""Audit logging backend that saves logs to a database."""

from sitech_audit_log.backends.base import BaseLoggingBackend


class DatabaseBackend(BaseLoggingBackend):

    def save(self, data):
        """
        Save the log for one or more Models objects
        """
        pass

