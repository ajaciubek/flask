# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116

class Calculator():
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def add(self) -> float:
        return self.__x + self.__y

    def substract(self) -> float:
        return self.__x - self.__y
