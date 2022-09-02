from pxlautopylot.action import Action
from pxlautopylot.color import Color
from pxlautopylot.pilotable import Pilotable
from pxlautopylot.pixel import Pixel


class Automation:

    def __init__(self, pixel: dict, color: dict, target_color: bool, actions: [Action]):
        self.pixel = Pixel(**pixel)
        self.color = Color(**color)
        self.target_color = target_color
        self.actions = []
        for action in actions:
            self.actions.append(Action(**action))

    def __str__(self):
        return "{{ 'pixel' : {0}, 'color' : {1}, 'target_color' : {2}, 'actions': {3} }}".format(self.pixel,
                                                                                                 self.color,
                                                                                                 self.target_color,
                                                                                                 self.actions)

    def run(self, pilotable: Pilotable):
        target_achieved = self.pixel.is_same_color(self.color) and self.target_color
        default_missing = not self.pixel.is_same_color(self.color) and not self.target_color
        if target_achieved or default_missing:
            for action in self.actions:
                action.execute(pilotable)
