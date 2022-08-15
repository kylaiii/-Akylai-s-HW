
class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def LCM(self, number1 , number2):
        return (self.LCM(number2, number1 % number2) if number2 else number1)

    def __add__(self, other):
        znam = self.denumerator * other.denumerator // self.LCM(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator + znam // other.denumerator * other.numerator
        return f"{chisl}/{znam}"

    def __sub__(self, other):
        znam = self.denumerator * other.denumerator // self.LCM(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator - znam // other.denumerator * other.numerator
        return f"{chisl}/{znam}"

    def __mul__(self, other):
        chisl = self.numerator * other.numerator
        znam = self.denumerator * other.denumerator
        nok = self.LCM(chisl,znam)
        chisl //= nok
        znam //= nok
        return f"{chisl}/{znam}"

    def __floordiv__(self, other):
        chisl = self.numerator * other.denumerator
        znam = other.numerator * self.denumerator
        nok = self.LCM(chisl, znam)
        chisl //= nok
        znam //= nok
        return f"{chisl}/{znam}"

number1 = [6,15]
number2 = [3,5]

num1 = Fraction(number1[0], number1[1])
num2 = Fraction(number2[0], number2[1])

print(f"{num1.numerator}/{num1.denumerator} + {num2.numerator}/{num2.denumerator} = {num1 + num2}")
print(f"{num1.numerator}/{num1.denumerator} - {num2.numerator}/{num2.denumerator} = {num1 - num2}")
print(f"{num1.numerator}/{num1.denumerator} * {num2.numerator}/{num2.denumerator} = {num1 * num2}")
print(f"{num1.numerator}/{num1.denumerator} // {num2.numerator}/{num2.denumerator} = {num1 // num2}")

