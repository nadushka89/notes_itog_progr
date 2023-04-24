
class ReadNote():
    def __init__(self, console):
        self.console = console
    @property
    def description(self):
        return "Открыть записную книжку"

    def execute(self):
        self.console.read_notebook()