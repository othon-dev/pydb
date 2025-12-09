class PyDBError(Exception):
    """Base exception for all PyDB errors."""


class PyDBFileError(PyDBError):
    """Exception raised for file-related errors in PyDB."""


class PyDBIndexError(PyDBError):
    """Exception raised for index-related errors in PyDB."""


class PyDBStorageError(PyDBError):
    """Exception raised for storage-related errors in PyDB."""
