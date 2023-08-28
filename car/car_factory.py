from car.car import Car
from datetime import date
from car.engine.capulet_engine import CapuletEngine
from car.engine.willoughby_engine import WilloughbyEngine
from car.engine.sternman_engine import SternmanEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)  
        return Car(engine)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage) 
        return Car(engine)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(last_service_date, warning_light_on) 
        return Car(engine)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)  
        return Car(engine)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)  
        return Car(engine)