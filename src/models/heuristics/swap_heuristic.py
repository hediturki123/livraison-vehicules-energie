import copy as cp

from src.models import Heuristic, Strategy, StrategyExecutionResult
from src.models.context import WAREHOUSE_POSITION


class SwapHeuristic(Heuristic):
    def __init__(self, strategy: Strategy):
        super().__init__(strategy)
        self.context = strategy.context

    def explore_neighborhood(self, min_dist: float, visits_to_do: list[int], first_solution: bool) -> (float, StrategyExecutionResult):
        strategy_result = StrategyExecutionResult(0, [], [])
        visits = cp.copy(visits_to_do)
        i = 0
        while i < len(visits_to_do):
            j = 1
            while j < len(visits_to_do):
                swapped_visits_to_do = self.swap_visits(i, j, cp.copy(visits_to_do))
                # On compare la distance totale parcourue en faisant l'insert par rapport à la distance initiale
                strategy_result = self.strategy.execute(swapped_visits_to_do)
                new_dist = strategy_result.total_driven_distance
                if new_dist < min_dist:
                    min_dist = new_dist
                    if first_solution:
                        return min_dist, strategy_result
                    else:
                        visits = strategy_result.visits_done
                j += 1
            i += 1
        strategy_result.visits_done = visits
        return min_dist, strategy_result

    @staticmethod
    def swap_visits(i: int, j: int, visits: list[int]) -> list[int]:
        visits[i], visits[j] = visits[j], visits[i]
        return visits
