"""simple tests for calculator
"""

from calculator import calculator


def test_add():
    assert 15 == calculator.add(7, 8)


def test_subtract():
    assert 3 == calculator.subtract(10, 7)
