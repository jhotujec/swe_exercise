import pytest

from lib import Calculator


class TestPrefixCalculator:
    data = [
        ('3', 3),
        ('+ 1 2', 3),
        ('+ 1 * 2 3', 7),
        ('+ * 1 2 3', 5),
        ('- / 10 + 1 1 * 1 2', 3),
        ('- 0 3', -3),
        ('/ 3 2', 1.5)
    ]

    @pytest.mark.parametrize("expression, result", data)
    def test_result(self, expression, result):
        calculator = Calculator()

        assert calculator.calculate(expression) == result


class TestInfixCalculator:
    data = [
        ('0', 0),
        ('0 + 0', 0),
        ('( 1 + 2 )', 3),
        ('( 1 + ( 2 * 3 ) )', 7),
        ('( ( 1 * 2 ) + 3 )', 5),
        ('+ * 1 2 3', 5),
        ('( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )', -1.8),
        ('5000 + 5000 + 5000', 15000)
    ]

    @pytest.mark.parametrize("expression, result", data)
    def test_result(self, expression, result):
        calculator = Calculator()

        assert calculator.calculate(expression, infix=True) == result
