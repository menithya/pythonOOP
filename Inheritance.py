class Person():
    def __init__(self,name, age, roll_number) -> None:
        self.age = age
        self.name = name
        self.roll_number = roll_number

    def get_name(self):
       print(f"Hello, name of the person is {self.name}")
    
    def get_age(self):
        return self.age
    
class Department(Person):
    def __init__(self, name, age, roll_number) -> None:
        super().__init__(name, age, roll_number)
        
    def get_name(self):
        super().get_name()


# print(help(Department))

dept = Department("nini",21,100)
print(dept.age)
dept.get_name()