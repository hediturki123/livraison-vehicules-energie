from src.models import Instance
from src.models.actions import Action


class DoNothing(Action):
    def __init__(self, instance: Instance):
        super().__init__(instance, 0.0, 0)

    def execute(self) -> None:
        pass

    def is_doable(self) -> bool:
        return True
