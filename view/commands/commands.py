""" Абстрактный класс Command"""
from abc import ABCMeta,abstractmethod


class Commands(ABCMeta):
    """Абстрактный базовый класс для всех команд"""

    @abstractmethod
    def description(self):
        """описание команды"""

    @abstractmethod
    def execute(self):
        """выполнение команды"""



