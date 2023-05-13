import copy as cp

from src.models import Heuristic, Strategy, StrategyExecutionResult
from src.models.context import WAREHOUSE_POSITION


class SwapHeuristic(Heuristic):
    def __init__(self, strategy: Strategy):
        super().__init__(strategy)
        self.context = strategy.context

    def explore_neighborhood(self, min_dist: float, visits_to_do: list[int], first_solution: bool) -> (list[int], float):
        visits = cp.copy(visits_to_do)
        i = 0
        while i < len(visits_to_do):
            j = 1
            while j < len(visits_to_do):
                swapped_visits_to_do = self.__swap_visits(i, j, cp.copy(visits_to_do))
                # On compare la distance totale parcourue en faisant l'insert par rapport à la distance initiale
                strategy_result = self.strategy.execute(swapped_visits_to_do)
                new_dist = strategy_result.total_driven_distance
                if new_dist < min_dist:
                    min_dist = new_dist
                    if first_solution:
                        return strategy_result.visits_done, min_dist
                    else:
                        visits = strategy_result.visits_done
                j += 1
            i += 1
        return visits, min_dist

    @staticmethod
    def __swap_visits(i: int, j: int, visits: list[int]) -> list[int]:
        visits[i], visits[j] = visits[j], visits[i]
        return visits
