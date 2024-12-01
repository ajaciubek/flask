from calculator import Calculator

def test_add():
    c = Calculator(1.5, 1.5)
    assert c.add() == 3.0
