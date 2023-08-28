from abc import ABC, abstractmethod

class IServiceCriteria(ABC):
    
    @abstractmethod
    def needs_service(self):
        pass