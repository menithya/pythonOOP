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
        self.name = name
        # self.age = age
        self.roll_number = roll_number
        
    # def get_name(self):
    #     super().get_name()


# print(help(Department))

dept = Department("nini",21,100)
print(dept.age)
dept.get_name()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, name, age, roll_no):
        # super().__init__(name, age) # Call the constructor of the parent class, if you do not call this method we will get attribue errr
        # becuase name attribute not exist in child class and we are not calling super().__init__
        self.roll_no = roll_no
   
    def get_roll_no(self):
        return self.roll_no

s = Student('John', 20, 123)
print(s.get_name()) # Output: John
print(s.get_roll_no()) # Output: 123