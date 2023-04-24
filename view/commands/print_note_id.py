""" Найти заметку по ID"""
from view.commands.commands import Commands

class Print_note_id():
    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Найти заметку по ID"

    def execute(self):
        self.console.print_note_id()