class Calculator(object):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def add(self) -> float:
        return self.__x + self.__y