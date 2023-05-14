import copy as cp

from src.models import Heuristic, Strategy


class TripletShiftHeuristic(Heuristic):
    def __init__(self, strategy: Strategy):
        super().__init__(strategy)
        self.context = strategy.context

    def explore_neighborhood(
            self,
            min_dist: float,
            visits_to_do: list[int],
            keep_first_solution: bool
    ) -> (list[int], float):
        visits = cp.copy(visits_to_do)
        i = 0
        while i < len(visits_to_do):
            j = 1
            while j < len(visits_to_do):
                inserted_visits_to_do = self.shift_visits(j, cp.copy(visits_to_do))
                strategy_result = self.strategy.execute(inserted_visits_to_do)
                new_dist = strategy_result.total_driven_distance
                if new_dist < min_dist:
                    min_dist = new_dist
                    if keep_first_solution:
                        return strategy_result.visits_done, min_dist
                    else:
                        visits = strategy_result.visits_done
                j += 1
            i += 1
        return visits, min_dist

    @staticmethod
    def shift_visits(source_index: int, visits: list[int]) -> list[int]:
        mod = len(visits)
        source_index = source_index % mod
        visits[source_index], visits[(source_index + 1) % mod], visits[(source_index + 2) % mod], visits[(source_index + 3) % mod] = visits[(source_index + 3) % mod], visits[source_index], visits[(source_index + 1) % mod], visits[(source_index + 2) % mod]
        return visits

