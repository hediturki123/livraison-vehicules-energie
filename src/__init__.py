from sys import argv

import click

from src.models import Strategy, Heuristic
from src.models.heuristics import SwapHeuristic, InsertHeuristic
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
    type=click.Choice(['insert', 'swap'], case_sensitive=False),
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
    '-v', '--verbose',
    is_flag=True,
    help="Print a full description of the results."
)
def main(instance_name: str, determinist: bool, heuristic: str, verbose: bool, charge_speed: str):
    context: Context = Context(instance_name, verbose, charge_speed)

    strategy: Strategy = BasicStrategy(context, is_determinist=determinist)

    chosen_heuristic: Heuristic | None = None
    match heuristic:
        case 'insert': chosen_heuristic = InsertHeuristic(strategy)
        case 'swap': chosen_heuristic = SwapHeuristic(strategy)
        case _: pass

    if chosen_heuristic is not None:
        chosen_heuristic.execute_strategy()
    else:
        click.echo("Please choose a valid heuristic.", err=True)


if __name__ == '__main__':
    main()
