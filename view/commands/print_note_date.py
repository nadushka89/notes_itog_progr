"""  Найти заметку по дате"""

from view.commands.commands import Commands

class Print_note_date():
    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Найти заметку по дате"

    def execute(self):
        self.console.print_note_date()