from presenter import presenter
from view.commands.menu import Menu
from view.validator import Validator
from view.view_abs import View

"""Взаимодействие с пользователем через консоль"""


class Console():
    __working = False
    __write = True
    __read = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def read_notebook(self):
         if not self.__read:
            self.presenter.read_file()
            self.__read=True
            if self.presenter.is_full():
                print("Записная книжка открыта.")
            else:
                print("К сожалению, в записной книжки нет записей.")
         else:
             print("Записная книжка уже открыта.")

    def all_print_notes(self):
        if self.presenter.is_full():
            print(self.presenter.get_notebook())
        else:
            print("\nК сожалению, в записной книжке еще нет записей или не открыта.")

    def delete_note(self):
        if self.presenter.is_full():
            index = Validator.get_index(self.presenter.get_size_notebook(),
                                        "\nВведите номер заметки,  который хотите удалить: ")
            self.presenter.delete_note(index)
            print("Заметка успешно удалена")
        else:
            print("\nК сожалению, в записной книжке еще нет записей или не открыта.")

    def update_note(self):
        if self.presenter.is_full():
            index = Validator.get_index(self.presenter.get_size_notebook(),
                                        "\nВведите номер заметки,  который хотите изменить: ")
            update_title_note =input ("\nВведите заголовок: ")
            update_body_note = input("\nВведите заметку: ")
            self.presenter.update_note(index, update_title_note, update_body_note)
            print("\nЗаметка успешно изменена")
        else:
            print("\nК сожалению, в записной книжке еще нет записей или не открыта.")

    def add_note(self):
        new_note_title = input("\nВведите заголовок: ")
        new_body_note =input ("\nВведите заметку: ")
        self.presenter.add_note(new_note_title, new_body_note)
        print("\nЗаметка успешно добавлена")

    def exit(self):
        if self.__write:
            self.__working = False
        print("Завершение работы")

    def save_file(self):
        self.presenter.write_file()
        self.__write= True
        print("Изменения сохранены в файл")


    def print_note_date(self):
        if self.presenter.is_full():
            date = input('Введите дату (формат: DD.MM.YYYY)\n')
            print(self.presenter.filter_by_date(date))
        else:
            print("\nК сожалению, в записной книжке еще нет записей")

    def print_note_id(self):
        if self.presenter.is_full():
            index = Validator.get_index(self.presenter.get_size_notebook(),
                                        "\nВведите номер заметки, который хотите посмотреть: ")
            print(self.presenter.find_by_id(index))
        else:
            print("\nК сожалению, в записной книжке еще нет записей")

    def start(self):
        self.__working = True
        menu = Menu(self)
        while self.__working:
            print(menu)
            index = Validator.get_index(menu.get_menu_size(), "\n Выберите пункт меню: ")
            menu.execute(index)
