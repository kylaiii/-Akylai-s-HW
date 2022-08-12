class Fraction:
    def __init__(self,numertor, denumerator):
        self.numertor = numertor
        self.denumerator = denumerator
        print(f'{self.numertor} / {self.denumerator}')

    def __add__(self, a, b):
       print(f"  Сложение: {self.numertor} / {self.denumerator} + {a} / {b}")
       print(f'Ответ: {self.numertor * b + a * self.denumerator} / {self.denumerator * b}')

    def __sub__(self, a, b):
        print(f"  Вычитание: {self.numertor} / {self.denumerator} - {a} / {b}")
        print(f'Ответ: {self.numertor * b - a * self.denumerator} / {self.denumerator * b}')

    def __floordiv__(self, a, b):
        print(f"  Деление: {self.numertor} / {self.denumerator} // {a} / {b}")
        print(f'Ответ: {self.numertor * b} / {self.denumerator * a }')

    def __mul__(self, a, b):
        print(f"  Умножение: {self.numertor} / {self.denumerator} * {a} / {b}")
        print(f'Ответ: {self.numertor * a} / {self.denumerator * b}')


numbers = Fraction(1, 3)

numbers.__add__(1,2)
numbers.__sub__(1,2)
numbers.__floordiv__(1,2)
numbers.__mul__(1,2)