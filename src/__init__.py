from sys import argv

from src.models import Strategy, Heuristic
from src.models.heuristics import SwapHeuristic
from src.models.strategies import BasicStrategy
from src.models.context import WAREHOUSE_POSITION, Context


def main():
    if len(argv) >= 2:
        instance_name: str = argv[1]

        context: Context = Context(instance_name)

        strategy: Strategy = BasicStrategy(context, is_determinist=False)

        heuristic: Heuristic = SwapHeuristic(strategy)

        heuristic.execute_strategy()
    else:
        print("Veuillez renseigner un nom d'instance en argument.")


if __name__ == '__main__':
    main()
