"""Audit Logging backend that saves logs to a file."""

from sitech_audit_log.backends.base import BaseLoggingBackend


class FileBackend(BaseLoggingBackend):

    def save(self, audit_log):
        """
        Save the log for one or more Models objects
        """
        pass

