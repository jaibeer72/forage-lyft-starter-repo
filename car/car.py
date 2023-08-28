from core.iEngine import IEngine


class Car:
    def __init__(self,  engine: IEngine,):
        self.engine = engine

    def needs_service(self):
        return self.engine.needs_service
