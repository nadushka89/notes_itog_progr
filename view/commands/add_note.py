from view.commands.commands import Commands
""" Добавление заметки"""

class Add_note():

    def __init__(self, console):
        self.console = console
    @property
    def description(self):
        return "Создать новую заметку"

    def execute(self):
        self.console.add_note()
