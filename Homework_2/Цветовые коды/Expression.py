class Expression:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def __str__(self):
        if self.op == '+':
            result = self.num1 + self.num2
        elif self.op == '-':
            result = self.num1 - self.num2
        elif self.op == '*':
            result = self.num1 * self.num2
        elif self.op == '/':
            result = self.num1 / self.num2
        else:
            result = None
        return f"{self.num1} {self.op} {self.num2} = {result}"

    def __repr__(self):
        return f"Expression({self.num1}, '{self.op}', {self.num2})"

    def __eq__(self, other):
        if not isinstance(other, Expression):
            return NotImplemented

        def get_result(expr):
            if expr.op == '+':
                return expr.num1 + expr.num2
            elif expr.op == '-':
                return expr.num1 - expr.num2
            elif expr.op == '*':
                return expr.num1 * expr.num2
            elif expr.op == '/':
                return expr.num1 / expr.num2
            else:
                return None

        return get_result(self) == get_result(other)

 
# Пример
expr1 = Expression(3, '+', 4)
expr2 = Expression(2, '*', 3.5)
expr3 = Expression(10, '-', 2)

print(str(expr1))          # 3 + 4 = 7
print(repr(expr1))         # Expression(3, '+', 4)
print(expr1 == expr2)      # True, потому что 7 == 7
print(expr1 == expr3)      # False, потому что 7 != 8