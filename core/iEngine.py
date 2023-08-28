from abc import ABC, abstractmethod
from datetime import datetime

class IEngine(ABC):
    def __init__(self, last_service_date): 
        self.last_service_date = last_service_date
        self.current_date = datetime.datetime.now()
