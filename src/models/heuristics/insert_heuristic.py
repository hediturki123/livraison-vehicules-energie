from src.models import Heuristic, Strategy, StrategyExecutionResult
from src.models.context import WAREHOUSE_POSITION


class InsertHeuristic(Heuristic):
    def __init__(self, strategy: Strategy):
        super().__init__(strategy)
        self.context = strategy.context

    def execute_strategy(self):
        visits_to_do: list[int] = [visit_id for visit_id in self.context.visits]
        visits_to_do.remove(WAREHOUSE_POSITION)
        # On récupère la distance totale parcourue pour toutes les visites
        strategy_result: StrategyExecutionResult = self.strategy.execute(visits_to_do)
        min_dist: float = strategy_result.total_driven_distance

        i = 0
        while i < len(visits_to_do):
            j = 1
            while j < len(visits_to_do):
                inserted_visits_to_do = self.__insert_visits(i, j, visits_to_do)
                # On compare la distance totale parcourue en faisant l'insert par rapport à la distance initiale
                strategy_result = self.strategy.execute(inserted_visits_to_do)
                new_dist = strategy_result.total_driven_distance
                if new_dist < min_dist:
                    min_dist = new_dist
                j += 1
            i += 1

        strategy_result.print_history()
        return min_dist

    @staticmethod
    def __insert_visits(i: int, j: int, visits: list[int]) -> list[int]:
        tmp = visits[i]
        visits.pop(i)
        visits.insert(j, tmp)
        return visits
