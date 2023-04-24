from model.notebook import Notebook
from model.notebook import Note


class FileReader:
    def __init__(self, path: str):
        self.path = path

    def read_note(self, notebook: Notebook):
        """Чтение заметок из файла"""
        try:
            with open(self.path, 'r', encoding='UTF-8') as data:
                notes = data.readlines()
                for note in notes:
                    note_list = note.strip().replace(' ', ';', 2).split(';')
                    notebook.get_notes().append(Note(note_list[0], note_list[1], note_list[2]))
        except FileNotFoundError:
            pass
        return notebook
    def write_note(self, notebook: Notebook):
        """Запись заметок в файл"""
        with open(self.path, 'w', encoding='UTF-8') as data:
            for note in notebook.get_notes():
                data.write(str(note) + '\n')