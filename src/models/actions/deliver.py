from src.models.actions.action import Action
from src.models.instance import Instance


class Deliver(Action):
    def __init__(self, instance: Instance, duration: int):
        super().__init__(instance, 0.0, duration)

    def execute(self):
        print("Le véhicule %d effectue sa livraison..." % self.instance.current_vehicle.ve_id)
        # TODO:


    def is_doable(self) -> bool:
        # TODO
        return True
