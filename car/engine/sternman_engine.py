from core.iServiceCriteria import IServiceCriteria
from core.iEngine import IEngine

class SternmanEngine(IEngine, IServiceCriteria):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
