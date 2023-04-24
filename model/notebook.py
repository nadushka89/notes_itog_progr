from datetime import datetime
from model.note import Note


class Notebook:

    def __init__(self):
        self.__notes = []

    def size(self):
        return len(self.__notes)

    def add_note(self, title, body):
        note = Note(str(datetime.today().strftime('%d.%m.%Y')), title, body)
        self.__notes.append(note)

    def update_note(self, index, new_title, new_body):
        self.__notes[index].update_note(new_title, new_body)

    def delete_note(self, index):
        del self.__notes[index]

    def find_by_id(self, index):
        return self.__notes[index]

    def filter_by_date(self, date):
        notes_str = "\nСписок заметок:\n"
        for i, note in enumerate(self.__notes, 1):
            if date in note.get_date():
                notes_str +=f"\t{i}. {note}\n"
        return notes_str

    def is_full(self):
        return bool(self.__notes)

    def __str__(self):
        notes_str = "\nСписок заметок:\n"
        for i, note in enumerate(self.__notes, 1):
            notes_str += f"\t{i}. {note}\n"
        return notes_str

    def get_notes(self):
        return self.__notes
