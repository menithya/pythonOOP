class Person():
    def __init__(self,age, name, roll_number) -> None:
        self.age = age
        self.name = name
        self.roll_number = roll_number

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
class Department(Person):
    pass


print(help(Department))