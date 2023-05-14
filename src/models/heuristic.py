from abc import abstractmethod, ABC

from src.models.strategy import Strategy
from src.models.strategy_execution_result import StrategyExecutionResult
from src.models.context import WAREHOUSE_POSITION


class Heuristic(ABC):
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.context = strategy.context

    @abstractmethod
    def explore_neighborhood(
        self,
        min_dist: float,
        visits_to_do: list[int],
        keep_first_solution: bool
    ) -> (float, StrategyExecutionResult):
        pass

    def execute_strategy(self):
        visits: list[int] = [visit_id for visit_id in self.context.visits]
        visits.remove(WAREHOUSE_POSITION)
        # On récupère la distance totale parcourue pour toutes les visites
        strategy_result: StrategyExecutionResult = self.strategy.execute(visits)

        visits_to_do: list[int] = strategy_result.visits_done
        min_dist: float = strategy_result.total_driven_distance
        last_min_dist: float = float('inf')

        iteration: int = 0
        while iteration < self.context.iteration_count and min_dist != last_min_dist:
            last_min_dist = min_dist
            min_dist, strategy_result = self.explore_neighborhood(min_dist, visits_to_do, self.context.keep_first_solution)
            visits_to_do = strategy_result.visits_done
            iteration += 1

        match self.context.output:
            case 'min_dist': print(last_min_dist)
            case 'history': strategy_result.print_history()

        return last_min_dist
