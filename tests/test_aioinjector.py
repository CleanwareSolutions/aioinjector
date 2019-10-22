from pytest import fixture
from aioinjector.aioinjector import AioInjector


class Engine():
    def __init__(self, **attributes):
        self.capacity: int = attributes.get('capacity', 1000)


class Car():
    def __init__(self, **attributes):
        self.model: int = attributes.get('model', 1990)
        self.engine: Engine = attributes["engine"]


@fixture
def engine() -> Engine:
    return Engine(capacity=150)


@fixture
def car(engine) -> Car:
    return Car(model=2019, engine=engine)


def test_aioinjector_engine_instance_creation(aioinjector: AioInjector):
    aioinjector.create(Engine)
    engine = aioinjector.instance(Engine)
    engine.capacity = 150
    assert aioinjector.instance(Engine).capacity == 150


def test_aioinjector_car_instance_creation(aioinjector: AioInjector):
    aioinjector.create(Engine)
    aioinjector.create(Car, engine=aioinjector.instance(Engine))
    assert aioinjector.instance(Car).engine.capacity == 1000
