import copy as cp

from src.models import Heuristic, Strategy, StrategyExecutionResult


class InsertHeuristic(Heuristic):
    def __init__(self, strategy: Strategy):
        super().__init__(strategy)
        self.context = strategy.context

    def explore_neighborhood(
            self,
            min_dist: float,
            visits_to_do: list[int],
            keep_first_solution: bool
    ) -> (float, StrategyExecutionResult):
        strategy_result = StrategyExecutionResult(0, [], [])
        visits = cp.copy(visits_to_do)
        i = 0
        while i < len(visits_to_do):
            j = 1
            while j < len(visits_to_do):
                inserted_visits_to_do = self.insert_visits(i, j, cp.copy(visits_to_do))
                strategy_result = self.strategy.execute(inserted_visits_to_do)
                new_dist = strategy_result.total_driven_distance
                if new_dist < min_dist:
                    min_dist = new_dist
                    if keep_first_solution:
                        return min_dist, strategy_result
                    else:
                        visits = strategy_result.visits_done
                j += 1
            i += 1
        strategy_result.visits_done = visits
        return min_dist, strategy_result

    @staticmethod
    def insert_visits(source_index: int, target_index: int, visits: list[int]) -> list[int]:
        if target_index >= len(visits):
            raise IndexError('target index should not exceed visits count')
        visits.insert(target_index, visits.pop(source_index))
        return visits
