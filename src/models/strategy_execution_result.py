class StrategyExecutionResult:
    def __init__(self, total_driven_distance: float, history: list[list[str]]):
        self.total_driven_distance = total_driven_distance
        self.history = history

    # Méthode d'affichage de l'historique des actions effectuées par la stratégie
    def print_history(self):
        for vehicle_round in self.history:
            print("%s" % ','.join(vehicle_round))
