from typing import List
from pytest import fixture
from aioinjector.aioinjector import AioInjector


# Testing with kwargs throw class

class Engine():
    def __init__(self, **attributes) -> None:
        self.capacity: int = attributes.get('capacity', 1000)


class Car():
    def __init__(self, **attributes) -> None:
        self.model: int = attributes.get('model', 1990)
        self.engine: Engine = attributes["engine"]


def test_aioinjector_engine_instance_creation(aioinjector: AioInjector):
    aioinjector.create(Engine)
    engine = aioinjector.instance(Engine)
    engine.capacity = 150
    assert aioinjector.instance(Engine).capacity == 150


def test_aioinjector_car_instance_creation(aioinjector: AioInjector):
    aioinjector.create(Engine)
    aioinjector.create(Car, engine=aioinjector.instance(Engine))
    assert aioinjector.instance(Car).engine.capacity == 1000


# Testing with class declarative attributes


class Employee():
    def __init__(self, name: str) -> None:
        self.name: str = name


class Work():
    def __init__(self, place: str, employees: List[Employee]):
        self.place: str = place
        self.employees: List[Employee] = employees


def test_aioinjector_employee_instance_creation(aioinjector: AioInjector):
    aioinjector.create(Employee, name="John Smith")
    assert aioinjector.instance(Employee).name == "John Smith"


def test_aioinjector_work_instance_creation(aioinjector: AioInjector):
    john_smith = Employee("John Smith")
    mike_summer = Employee("Mike Summer")
    aioinjector.create(
        Work, place="Michigan", employees=[john_smith, mike_summer])
    assert len(aioinjector.instance(Work).employees) == 2
