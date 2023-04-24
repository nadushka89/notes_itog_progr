"""Класс обрабатывает пользовательский ввод"""

class Validator:
    def __init__(self):
        self.presenter = None

    @staticmethod
    def get_index(size, text):
        """Индекс для списка меню"""
        while True:
            user_answer = input(text)
            if (user_answer.isdigit() and 1<=int(user_answer)<=size):
                index = int(user_answer)-1
                return index
            print(f"\nВы ввели некорректное число. Введите число от 1 до {size}")
