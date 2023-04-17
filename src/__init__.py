from sys import argv

from src.models import Strategy
from src.models.strategies.determinist_strategy import DeterministStrategy
from src.models.context import WAREHOUSE_POSITION, Context


def main():
    if len(argv) >= 2:
        instance_name: str = argv[1]

        context: Context = Context(instance_name)

        strategy: Strategy = DeterministStrategy(context)

        visits_to_do: list[int] = [visits for visits in context.visits]
        visits_to_do.remove(WAREHOUSE_POSITION)

        result = strategy.execute(visits_to_do)

        print('\nDistance totale parcourue : %.3f km' % result)
    else:
        print("Veuillez renseigner un nom d'instance en argument.")


if __name__ == '__main__':
    main()
