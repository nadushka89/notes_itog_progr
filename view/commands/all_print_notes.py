""" Показать все заметки """

from view.commands.commands import Commands

class All_print_notes():
    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Показать все заметки "

    def execute(self):
        self.console.all_print_notes()
