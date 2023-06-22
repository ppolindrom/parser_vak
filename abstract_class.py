from abc import ABC, abstractmethod


class AbstractJobPlatform(ABC):
    """абстрактный класс, обязывающий создание методов в других классах-наследниках"""
    @abstractmethod
    def server_connection(self):
        pass

    @abstractmethod
    def job_dictionary(self, query):
        pass

    @abstractmethod
    def file_vacancy(self, jobs):
        pass
