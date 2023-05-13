from sys import argv

import click

from src.models import Strategy, Heuristic
from src.models.heuristics import SwapHeuristic, InsertHeuristic
from src.models.heuristics.permutation_heuristic import PermutationHeuristic
from src.models.strategies import BasicStrategy
from src.models.context import WAREHOUSE_POSITION, Context


@click.command()
@click.argument('instance_name')
@click.option(
    '-d/-nd', '--determinist/--non-determinist',
    default=True,
    show_default=True,
    help="Whether the strategy in heuristics should be deterministic or nondeterministic."
)
@click.option(
    '-h', '--heuristic',
    type=click.Choice(['insert', 'swap', 'permute'], case_sensitive=False),
    required=True,
    help="Define the heuristic to use (cf. README)."
)
@click.option(
    '-s', '--charge-speed',
    type=click.Choice(['slow', 'medium', 'fast'], case_sensitive=False),
    default='medium',
    show_default=True,
    help="Whether the charge speed of the vehicles should be slow, medium or fast."
)
@click.option(
    '-t', '--charge-threshold',
    type=click.FloatRange(0.00, 1.00),
    default=0.20,
    show_default=True,
    help="The threshold at which a vehicle should go back to the warehouse to charge."
)
@click.option(
    '-i', '--iteration-count',
    type=click.IntRange(1),
    default=100,
    show_default=True,
    help="The number of iteration to explore the solution neighborhood."
)
@click.option(
    '-fs/-bs', '--first-solution/--best-solution',
    default=True,
    show_default=True,
    help="Whether the algorithm stops at the first solution encountered or keeps running to find the best solution."
)
@click.option(
    '-v', '--verbose',
    is_flag=True,
    help="Print a full description of the results."
)
def main(
    instance_name: str,
    determinist: bool,
    heuristic: str,
    charge_speed: str,
    charge_threshold: float,
    iteration_count: int,
    first_solution: bool,
    verbose: bool
):
    context: Context = Context(instance_name, charge_speed, charge_threshold, first_solution, verbose)

    strategy: Strategy = BasicStrategy(context, is_determinist=determinist)

    print(iteration_count)

    chosen_heuristic: Heuristic | None = None
    match heuristic:
        case 'insert': chosen_heuristic = InsertHeuristic(strategy)
        case 'swap': chosen_heuristic = SwapHeuristic(strategy)
        case 'permute': chosen_heuristic = PermutationHeuristic(strategy)
        case _: pass

    if chosen_heuristic is not None:
        chosen_heuristic.execute_strategy()
    else:
        click.echo("Please choose a valid heuristic.", err=True)


if __name__ == '__main__':
    main()
