from model.filereader import FileReader
from model.notebook import Notebook
from model.note import Note

class Presenter:

    def __init__(self, view, notebook, path):
        self.__view = view
        self.__notebook = notebook
        self.__view.set_presenter(self)
        self.file = FileReader(path)

    def read_file(self):
        self.__notebook=self.file.read_note(self.__notebook)

    def write_file(self):
        self.file.write_note(self.__notebook)

    def is_full(self):
        return self.__notebook.is_full()

    def add_note(self, title, body):
        self.__notebook.add_note(title, body)

    def update_note(self, index, new_title, new_body):
        self.__notebook.update_note(index, new_title, new_body)

    def delete_note(self, index):
        self.__notebook.delete_note(index)

    def find_by_id(self, index):
        return self.__notebook.find_by_id(index)

    def filter_by_date(self, date):
        return self.__notebook.filter_by_date(date)

    def get_size_notebook(self):
        return self.__notebook.size()

    def get_notebook(self):
        return self.__notebook
