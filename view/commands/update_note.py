""" Изменить заметку """

from view.commands.commands import Commands

class Update_note():
    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Изменить заметку "

    def execute(self):
        self.console.update_note()
