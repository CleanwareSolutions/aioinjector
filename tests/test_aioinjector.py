import asyncio
from typing import List
from pytest import fixture
from aioinjector.aioinjector import AioInjector


@fixture
def aioinjector() -> AioInjector:
    return AioInjector()


# Testing with kwargs throw class

class Engine():
    def __init__(self, **attributes) -> None:
        self.capacity: int = attributes.get('capacity', 1000)


class Car():
    def __init__(self, **attributes) -> None:
        self.model: int = attributes.get('model', 1990)
        self.engine: Engine = attributes["engine"]


def test_aioinjector_engine_instance_creation(aioinjector: AioInjector):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aioinjector.create(Engine))
    engine = loop.run_until_complete(aioinjector.instance(Engine))
    engine.capacity = 150
    if loop.run_until_complete(
            aioinjector.instance(Engine)).capacity != 150:
        raise AssertionError("Engine capacity must be 150.")


def test_aioinjector_car_instance_creation(aioinjector: AioInjector):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aioinjector.create(Engine))
    loop.run_until_complete(aioinjector.create(
        Car, engine=aioinjector.instance(Engine)))
    print("Car::::", vars(loop.run_until_complete(
        aioinjector.instance(Car))))
    if loop.run_until_complete(loop.run_until_complete(
            aioinjector.instance(Car)).engine).capacity != 1000:
        raise AssertionError("Engine capacity must be 1000.")

# Testing with class declarative attributes


class Employee():
    def __init__(self, name: str) -> None:
        self.name: str = name


class Work():
    def __init__(self, place: str, employees: List[Employee]):
        self.place: str = place
        self.employees: List[Employee] = employees


def test_aioinjector_employee_instance_creation(aioinjector: AioInjector):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aioinjector.create(Employee, name="John Smith"))
    if loop.run_until_complete(
            aioinjector.instance(Employee)).name != "John Smith":
        raise AssertionError("Employee name must be John Smith.")


def test_aioinjector_work_instance_creation(aioinjector: AioInjector):
    john_smith = Employee("John Smith")
    mike_summer = Employee("Mike Summer")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aioinjector.create(
        Work, place="Michigan", employees=[john_smith, mike_summer]))
    if len(loop.run_until_complete(
            aioinjector.instance(Work)).employees) != 2:
        raise AssertionError("Work must have 2 employees.")
