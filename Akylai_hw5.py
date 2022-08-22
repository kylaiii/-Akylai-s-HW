import re
class ValidCarNumber:
    number = input("Введите номер по шаблону (01KG777ABC):")
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        is_valid = re.search(r"0[0-9]KG([0-9]{3})([A-Z]{3})", self.number)
        try:
            if self.number[0:is_valid.end()] == self.number:
              print("Номер валидный!")
        except:
           print("Номер не валидный!")

carnumber = ValidCarNumber()
carnumber.is_valid()
