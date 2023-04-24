""" Удалить заметку"""

from view.commands.commands import Commands

class Delete_note():
    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Удалить заметку"

    def execute(self):
        self.console.delete_note()