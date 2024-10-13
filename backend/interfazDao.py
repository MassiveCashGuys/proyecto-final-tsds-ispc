from abc import ABC, abstractmethod

class DataAccesDao(ABC):
    @abstractmethod
    def create(self,object):
        pass

    @abstractmethod
    def get(self, id_object):
        pass
    
    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, id_object):
        pass

   