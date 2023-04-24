""" Выход из приложения"""

from view.commands.commands import Commands

class Exit():
    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Выход из приложения"

    def execute(self):
        self.console.exit()