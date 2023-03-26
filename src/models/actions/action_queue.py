import copy
from typing import Iterable

from src.models import Instance
from src.models.actions.action import Action
from src.models.actions.do_nothing import DoNothing


class ActionQueue(list[Action], Action):
    def __init__(self, instance: Instance, iterable: Iterable[Action]):
        list[Action].extend(self, iterable)
        Action.__init__(
            self,
            instance,
            sum([action.distance for action in self]),
            sum([action.duration for action in self])
        )

    def execute(self) -> None:
        if self.is_doable():
            for action in self:
                action.execute()

    def is_doable(self) -> bool:
        is_doable: bool = True
        previous_action: Action = DoNothing(self.instance)
        for action in self:
            new_action: Action = copy.copy(action)
            new_action.distance = action.distance + previous_action.distance
            new_action.duration = action.duration + previous_action.duration
            is_doable = is_doable and new_action.is_doable()
            previous_action = new_action
            if not is_doable:
                break
        return is_doable
