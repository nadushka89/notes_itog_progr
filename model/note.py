from datetime import datetime


class Note:
    def __init__(self, date, title, body, ):
        self.__date = date
        self.__title = title
        self.__body = body


    def __str__(self):
        return f"{self.__date} {self.__title} {self.__body}"

    def update_note(self, update_title_note: str, update_body_note: str):
        self.__title = update_title_note
        self.__body = update_body_note

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def get_date(self):
        return self.__date



