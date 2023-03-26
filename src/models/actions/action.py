from abc import ABC, abstractmethod
from src.models import Instance


class Action(ABC):
    def __init__(self, instance, distance: float, duration: int):
        self.instance: Instance = instance
        self.distance: float = distance
        self.duration: int = duration

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def is_doable(self) -> bool:
        pass
