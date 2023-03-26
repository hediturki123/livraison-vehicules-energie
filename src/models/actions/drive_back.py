from src.models.actions.action import Action
from src.models.instance import Instance


class DriveBack(Action):
    def __init__(self, instance: Instance, distance: float, duration: int):
        super().__init__(instance, distance, duration)

    def execute(self):
        print(
            "Le véhicule %d parcourt %.1f km pendant %.1f pour revenir à l'entrepôt." %
            (self.instance.current_vehicle.ve_id, self.distance, self.duration)
        )
        # TODO

    def is_doable(self) -> bool:
        # TODO
        return True
