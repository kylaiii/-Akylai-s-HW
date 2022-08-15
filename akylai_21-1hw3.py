
class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def GCD(self, number1 , number2):
        return (self.GCD(number2, number1 % number2) if number2 else number1)

    def __add__(self, other):
        znam = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator + znam // other.denumerator * other.numerator
        return f"{chisl}/{znam}"

    def __sub__(self, other):
        znam = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator - znam // other.denumerator * other.numerator
        return f"{chisl}/{znam}"

    def __mul__(self, other):
        chisl = self.numerator * other.numerator
        znam = self.denumerator * other.denumerator
        return f"{chisl}/{znam}"

    def __floordiv__(self, other):
        chisl = self.numerator * other.denumerator
        znam = other.numerator * self.denumerator
        return f"{chisl}/{znam}"

number1 = 2,4
number2 = 1,2

num1 = Fraction(number1[0], number1[1])
num2 = Fraction(number2[0], number2[1])

print(f"{num1.numerator}/{num1.denumerator} + {num2.numerator}/{num2.denumerator} = {num1 + num2}")
print(f"{num1.numerator}/{num1.denumerator} - {num2.numerator}/{num2.denumerator} = {num1 - num2}")
print(f"{num1.numerator}/{num1.denumerator} * {num2.numerator}/{num2.denumerator} = {num1 * num2}")
print(f"{num1.numerator}/{num1.denumerator} // {num2.numerator}/{num2.denumerator} = {num1 // num2}")

