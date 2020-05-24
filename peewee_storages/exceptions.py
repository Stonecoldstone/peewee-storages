

class PeeweeStoragesException(Exception):
    pass


class StorageException(PeeweeStoragesException):
    pass


class StorageMissingConfig(StorageException):
    pass


class FileFieldException(PeeweeStoragesException):
    pass
