import copy

from src.models import Strategy, StrategyExecutionResult, Vehicle, Context
from src.models.context import WAREHOUSE_POSITION


class DeterministStrategy(Strategy):
    def __init__(self, context: Context):
        super().__init__(context)

    def execute(self, visits: list[int]) -> StrategyExecutionResult:
        # On recopie la liste des visites pour préserver l'entrée
        visits_to_do: list[int] = copy.copy(visits)

        # On crée un nouveau véhicule
        current_vehicle: Vehicle = Vehicle(self.context)
        used_vehicles: list[Vehicle] = [current_vehicle]
        # On ne charge PAS le véhicule (on le fait avant le départ du pilote du véhicule).
        # Tant qu'il y a des visites à effectuer...
        while len(visits_to_do) > 0:
            # La prochaine visite à effectuer est la première de la liste
            next_visit: int = visits_to_do[0]
            # Si le véhicule peut se déplacer, livrer puis rentrer
            if current_vehicle.can_move_and_deliver(next_visit, self.context.visits[next_visit].demand):
                # Se déplacer puis livrer
                current_vehicle.move_to(next_visit)
                current_vehicle.deliver(self.context.visits[next_visit].demand)
                # On enlève la visite de la liste des visites à effectuer
                visits_to_do.remove(next_visit)
            else:
                # Rentrer au dépôt
                current_vehicle.move_to(WAREHOUSE_POSITION)
                # Si le véhicule a besoin d'être rechargé
                if current_vehicle.needs_recharge():
                    # Recharger le véhicule
                    current_vehicle.recharge()
                current_vehicle.fill()
                # Si le véhicule peut se déplacer, livrer puis rentrer
                if current_vehicle.can_move_and_deliver(next_visit, self.context.visits[next_visit].demand):
                    # Se déplacer puis livrer
                    current_vehicle.move_to(next_visit)
                    current_vehicle.deliver(self.context.visits[next_visit].demand)
                    # On enlève la visite de la liste des visites à effectuer
                    visits_to_do.remove(next_visit)
                else:
                    # On change de véhicule
                    current_vehicle = Vehicle(self.context)
                    used_vehicles.append(current_vehicle)
        # Rentrer pour terminer la journée
        current_vehicle.move_to(0)

        # On affiche l'historique de conduite des véhicules et on calcule la distance totale parcourue
        total_distance: float = 0.0
        for vehicle in used_vehicles:
            total_distance += vehicle.total_driven_dist

        # On retourne la distance totale parcourue pour l'utiliser dans une heuristique
        return StrategyExecutionResult(total_distance, [vehicle.history for vehicle in used_vehicles])
