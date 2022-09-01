from pywinauto import findwindows, application
from pywinauto.findbestmatch import MatchError
from pxlautopylot.automation import Automation
from pxlautopylot.pilotable import Pilotable


class Autopilot(Pilotable):

    def __init__(self, window_name: str, description: str, debug: bool, automations: [Automation]):
        super().__init__()
        self.window_name = window_name
        self.description = description
        self.debug = debug
        self.automations = []
        for automation in automations:
            self.automations.append(Automation(**automation))
        self.should_run = False

    def __str__(self):
        return "{{ 'window_name': '{0}', 'description': '{1}', 'automations': {2} }}".format(self.window_name,
                                                                                             self.description,
                                                                                             self.automations)

    def log(self, message):
        if self.debug:
            print(message)

    def stop(self):
        self.should_run = False

    def launch(self):
        try:
            handle = findwindows.find_window(best_match=self.window_name)
            app = application.Application()
            app.connect(handle=handle)
            w_dialog = app[self.window_name]
            self.should_run = True
            while self.should_run:
                w_dialog.set_focus()
                for automation in self.automations:
                    automation.run(self)
        except MatchError:
            print("Could not find window {0}".format(self.window_name))
