import asyncio
from typing import Dict, TypeVar

T = TypeVar("T")


class AioInjector:
    def __init__(self) -> None:
        self.instances: Dict[str, T] = {}

    async def create(self, cls: T, **dependencies) -> T:
        self.instances[f"{cls.__name__},{cls.__name__}"] = cls(**dependencies)

    async def instance(self, cls: T) -> T:
        return self.instances[f"{cls.__name__},{cls.__name__}"]
