from abc import ABC, abstractmethod


class AbstractJobPlatform(ABC):
    @abstractmethod
    def server_connection(self):
        pass

    @abstractmethod
    def job_dictionary(self, query):
        pass

    @abstractmethod
    def file_vacancy(self, jobs):
        pass
