from abc import ABC, abstractmethod

from src.models.context import Context


class Strategy(ABC):
    def __init__(self, context: Context):
        self.context = context

    # Méthode d'exécution de la stratégie
    @abstractmethod
    def execute(self, visits_to_do: list[int]) -> float:
        pass
