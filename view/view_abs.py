"""Абстрактный класс View"""

from abc import ABCMeta, abstractmethod


class View(ABCMeta):
    @abstractmethod
    def set_presenter(self, presenter):
        """
        Aбстрактный метод, который принимает экземпляр класса-презентера
        (Presenter) в качестве аргумента.
        """

    @abstractmethod
    def start(self):
        """
        Aбстрактный метод, который должен выполнять начальную настройку представления и
        запускать его отображение.
        """
