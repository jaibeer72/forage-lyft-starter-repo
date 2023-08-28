from core.iEngine import IEngine
from core.iServiceCriteria import IServiceCriteria


class CapuletEngine(IEngine , IServiceCriteria):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 30000:
            return True
        else:
            return False
