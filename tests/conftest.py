from pytest import fixture
from aioinjector.aioinjector import AioInjector


@fixture
def aioinjector() -> AioInjector:
    return AioInjector()
