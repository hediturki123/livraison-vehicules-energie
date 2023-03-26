from src.models.actions.action import Action
from src.models.instance import Instance


class Recharge(Action):
    def __init__(self, instance: Instance, duration: int):
        super().__init__(instance, 0.0, duration)

    def execute(self):
        # TODO:
        pass

    def is_doable(self) -> bool:
        # TODO
        return True
