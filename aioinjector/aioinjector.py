import asyncio
from typing import Dict, Any, TypeVar

T = TypeVar("T")


class AioInjector:
    def __init__(self) -> None:
        self.instances: Dict[str, T] = {}

    def create(self, cls: T, **dependencies) -> T:
        self.instances[cls.__name__] = cls(**dependencies)
        # if len(dependencies) > 0:
        #     self.instances[cls.__name__] = cls(**dependencies)
        # else:
        #     self.instances[cls.__name__] = cls()

    def instance(self, cls: T) -> T:
        return self.instances[cls.__name__]
