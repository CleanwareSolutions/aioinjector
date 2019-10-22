import asyncio
from typing import Dict, Any, TypeVar

T = TypeVar("T")


class AioInjector:
    def __init__(self) -> None:
        self.instances: Dict[str, T] = {}

    def create(self, cls: T, **dependencies) -> T:
        self.instances[f"{cls.__name__},{cls.__name__}"] = cls(**dependencies)

    def instance(self, cls: T) -> T:
        return self.instances[f"{cls.__name__},{cls.__name__}"]
