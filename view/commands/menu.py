from view.commands.add_note import Add_note
from view.commands.all_print_notes import All_print_notes
from view.commands.delete_note import Delete_note
from view.commands.exit import Exit
from view.commands.print_note_date import Print_note_date
from view.commands.print_note_id import Print_note_id
from view.commands.update_note import Update_note
from view.commands.read_note import ReadNote
from view.commands.write_note import WriteAndSaveNote

"""Реализует запуск методов через меню"""


class Menu:
    def __init__(self, console):
        self.commands = []
        self.commands.append(ReadNote(console))
        self.commands.append(All_print_notes(console))
        self.commands.append(Add_note(console))
        self.commands.append(Print_note_id(console))
        self.commands.append(Print_note_date(console))
        self.commands.append(Update_note(console))
        self.commands.append(Delete_note(console))
        self.commands.append(WriteAndSaveNote(console))
        self.commands.append(Exit(console))

    def __str__(self):
        menu_str = "\n--------Главное меню:--------\n"
        for i, command in enumerate(self.commands, 1):
            menu_str += f"\t{i}. {command.description}\n"
        return menu_str

    def get_menu_size(self):
        return len(self.commands)

    def execute(self, index):
        cmd = self.commands[index]
        cmd.execute()
