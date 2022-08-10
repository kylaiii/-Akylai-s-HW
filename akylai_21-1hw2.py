class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name
class Person(Company):
    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.company_bank <= self.salary:
            print("У компании не достаточно средств!")
        else:
            print(f'Капитал после выдачи зп: {self.company_bank - self.salary}')

    def person_info(self):
        print(self.first_name, self.last_name, self.salary)

person1 = Person(45000, 'Bank of KR','Ivan','Ivanov',10000)
person1.get_salary()
person1.person_info()
