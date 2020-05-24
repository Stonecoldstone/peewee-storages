from abc import ABC, abstractmethod


class Storage(ABC):
    """ Base class for all the Storage backends.

    Provides basic interface for storages.

    """

    def __init__(self, *args, **kwargs):
        """ Storage Init """
        self.storage_options = kwargs

    def normailize_filename(self, filename):
        """ Returns filename valid for given storage engine. """
        return filename

    @abstractmethod
    def _store(self, safe_filename, data, *args, **kwargs):
        """ Subclass specific method to execute store operation.

        Parameters
        ----------
        safe_filename: str
            normalized filename that will be save for backend engine
        data: file
            filelike object

        """
        raise NotImplementedError("Store operation not defined. ")

    def store(self, filename, file_data, *args, **kwargs):
        """ Stores passed data

        Parameters
        ----------
        filename: str
            name for the file
        file_data: file
            readable binary object that will be stored
        """
        filename = self.normailize_filename(filename)
        return self._store(filename, file_data, *args, **kwargs)

    @abstractmethod
    def _load(self, safe_filename, *args, **kwargs):
        """ Subclass specific method to execute load operation.

        Parameters
        ----------
        safe_filename: str
            normalized filename that will be load from backend engine
        """
        raise NotImplementedError("Load operation not defined. ")

    def load(self, filename, *args, **kwargs):
        """ Loads file from engine by passed filename

        Parameters
        ----------
        filename: str
            name of the file
        """
        filename = self.normailize_filename(filename)
        return self._load(filename, *args, **kwargs)

    @abstractmethod
    def _remove(self, safe_filename, *args, **kwargs):
        """ Subclass specific method to execute remove operation.

        Parameters
        ----------
        safe_filename: str
            normalized filename that will be removed from backend engine
        """
        raise NotImplementedError("Remove operation not defined. ")

    def remove(self, filename, *args, **kwargs):
        """ Removes file from engine by passed filename

        Parameters
        ----------
        filename: str
            name of the file
        """
        filename = self.normailize_filename(filename)
        return self._remove(filename, *args, **kwargs)

    # remove alias
    delete = remove

    @abstractmethod
    def _find(self, safe_filename, *args, **kwargs):
        """ Subclass specific method to execute find operation.

        Parameters
        ----------
        safe_filename: str
            normalized filename that should be find.
        """
        raise NotImplementedError("Find operation not defined. ")

    def find(self, filename, *args, **kwargs):
        """ Finds file in engine by passed filename

        Parameters
        ----------
        filename: str
            name of the file
        """
        filename = self.normailize_filename(filename)
        return self._find(filename, *args, **kwargs)

    def exists(self, filename, **kwargs):
        """ Cheks if file exists in given storage

        Parameters
        ----------
        filename: str
            name of the file
        """
        return self.find(filename) is not None

    @abstractmethod
    def _list_storage(self):
        """ Generates listing of files inside given storage """
        raise NotImplementedError("Listing operation not defined.")

    def uri(self, filename):
        """
        Return a storage specific URI where the file can be retrieved.
        """
        raise NotImplementedError("This backend doesn't support URI location.")

    @abstractmethod
    def _metadata(self, safe_filename, *args, **kwargs):
        """ Subclass specific method to execute metadata lookup operation.

        Parameters
        ----------
        safe_filename: str
            normalized filename that will be check at backend.
        """
        raise NotImplementedError("Metadata retrive operation not defined. ")

    def metadata(self, filename, *args, **kwargs):
        """ Fetches metadata about file from engine.

        Parameters
        ----------
        filename: str
            name of the file
        """
        filename = self.normailize_filename(filename)
        return self._metadata(filename, *args, **kwargs)

    # metadata alias
    meta = metadata

    def __iter__(self):
        return self._list_storage()
