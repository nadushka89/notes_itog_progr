
class WriteAndSaveNote():
    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Сохранить и записать книжку в файл"


    def execute(self):
        self.console.save_file()