from abc import abstractmethod, ABC

from src.models.strategy import Strategy


class Heuristic(ABC):
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    @abstractmethod
    def execute_strategy(self) -> None:
        pass
