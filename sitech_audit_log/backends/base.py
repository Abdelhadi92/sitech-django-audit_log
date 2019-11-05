"""Base Audit logging backend class."""
from abc import ABC, abstractmethod


class BaseLoggingBackend(ABC):
    """
    Base class for Audit logging backend implementations.

    Subclasses must at least overwrite save().
    """

    @abstractmethod
    def save(self, audit_log):
        """
        Save the log for one or more Models objects
        """
        pass
