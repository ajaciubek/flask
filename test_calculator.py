# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116

from calculator import Calculator

def test_add():
    c = Calculator(1.5, 1.5)
    assert c.add() == 3.0


def test_substract():
    c = Calculator(2.0, 1.5)
    assert c.substract() == 0.5
