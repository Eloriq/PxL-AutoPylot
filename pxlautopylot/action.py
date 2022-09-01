from enum import Enum
from pxlautopylot.inputs import *
from pxlautopylot.pilotable import Pilotable


class ActionType(Enum):
    KEY = 1
    KEY_PRESS = 2
    KEY_RELEASE = 3
    CLICK = 4
    CLICK_PRESS = 5
    CLICK_RELEASE = 6
    MOVE = 7
    STOP = 8


class Action:
    ACTION_HANDLERS = {
        ActionType.KEY: lambda args: simulate_key(args['key']),
        ActionType.KEY_PRESS: lambda args: simulate_key_press(args['key']),
        ActionType.KEY_RELEASE: lambda args: simulate_key_release(args['key']),
        ActionType.CLICK: lambda args: simulate_click(args['x'], args['y']),
        ActionType.CLICK_PRESS: lambda args: simulate_click_press(args['x'], args['y']),
        ActionType.CLICK_RELEASE: lambda args: simulate_click_release(args['x'], args['y']),
        ActionType.MOVE: lambda args: move_mouse(args['x'], args['y'])
    }

    def __init__(self, action_type: str, args: dict):
        self.action_type = action_type
        self.args = args

    def __str__(self):
        return "{{ 'type' : {0}, 'args' : {1} }}".format(self.action_type, self.args)

    def execute(self, pilotable: Pilotable):
        action_type = ActionType[self.action_type.upper()]
        pilotable.log("{} action".format(action_type))
        if action_type == ActionType.STOP:
            pilotable.log(self.args['message'])
            pilotable.stop()
        else:
            handle = Action.ACTION_HANDLERS[action_type]
            handle(self.args)
