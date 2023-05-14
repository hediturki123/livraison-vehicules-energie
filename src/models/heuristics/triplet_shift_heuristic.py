import copy as cp

from src.models import Heuristic, Strategy, StrategyExecutionResult


class TripletShiftHeuristic(Heuristic):
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
                shifted_visits_to_do = self.shift_visits(j, cp.copy(visits_to_do))
                strategy_result = self.strategy.execute(shifted_visits_to_do)
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
    def shift_visits(source_index: int, visits: list[int]) -> list[int]:
        mod = len(visits)
        source_index = source_index % mod
        visits[source_index], visits[(source_index + 1) % mod], visits[(source_index + 2) % mod], visits[(source_index + 3) % mod] = visits[(source_index + 3) % mod], visits[source_index], visits[(source_index + 1) % mod], visits[(source_index + 2) % mod]
        return visits

