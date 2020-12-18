import logging


class Calculator:
    """
    A simple calculator capable of doing basic arithmetics. Supports `prefix` and
    `infix` expression notation using `stack` data type.

    HOW TO USE:
    1) Using `prefix` notation:
    > calculator = Calculator()
    > calculator.calculate('+ 1 2')
    > 3

    2) Using `infix` notation:
    > calculator = Calculator()
    > calculator.calculate('1 + 2', infix=True)
    > 3

    NOTE: Lots of the code below could be simplified by using `eval`, thought I don't
    think that is the point of an exercise. It is also unsafe in production.
    """

    # List of supported operators and their precedence inside expression.
    OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '(': None, ')': None}

    def __init__(self):
        self.stack = []
        self.logger = logging.getLogger(__name__)

    def infix_to_prefix(self, infix: list) -> list:
        """
        Transform infix expression notation to prefix by calculating postfix
        notation and then simply reversing the result.
        :param infix:
        :return:
        """
        # Start with empty result list.
        output = []

        # Prepare `infix` notation by replacing parentheses and reversing
        # original expression.
        infix = infix[::-1]
        for i, val in enumerate(infix):
            if val == ')':
                infix[i] = '('
            elif val == '(':
                infix[i] = ')'

        # Calculate `postfix` of an `infix` expression.
        for ch in infix:
            if ch not in self.OPERATORS.keys():
                output.append(ch)
            elif ch == '(':
                self.stack.append('(')
            elif ch == ')':
                while self.stack and self.stack[-1] != '(':
                    output += self.stack.pop()
                self.stack.pop()
            else:
                while self.stack and self.stack[-1] != '(' and self.OPERATORS[ch] <= self.OPERATORS[self.stack[-1]]:
                    output += self.stack.pop()
                self.stack.append(ch)

        while self.stack:
            output += self.stack.pop()

        return output[::-1]

    def evaluate(self, prefix: list) -> int:
        """
        Calculate result from prefix notation using stack (list) manipulation.
        :param prefix: Expression in prefix notation.
        :return: int
        """
        for operand in reversed(prefix):
            if operand is '+':
                self.stack[-2:] = [self.stack[-1] + self.stack[-2]]
            elif operand is '-':
                self.stack[-2:] = [self.stack[-1] - self.stack[-2]]
            elif operand is '*':
                self.stack[-2:] = [self.stack[-1] * self.stack[-2]]
            elif operand is '/':
                self.stack[-2:] = [self.stack[-1] / self.stack[-2]]
            else:
                self.stack.append(operand)

        return self.stack[0]

    @staticmethod
    def normalize_input(exp):
        """
        Normalize the input. Cast strings to integers; split the string by whitespace.
        :param exp:
        :return:
        """
        return [int(i) if i.isdigit() else i for i in exp]

    def calculate(self, exp, infix=False):
        """
        Calculate the expression.
        :param exp:
        :param infix:
        :return:
        """
        exp = exp.split()
        assert type(exp) is list

        if infix:
            exp = self.infix_to_prefix(exp)

        normalized_exp = self.normalize_input(exp)
        return self.evaluate(normalized_exp)


a = Calculator()
print(a.calculate('( 3 + 3 ) * 3', infix=True))
