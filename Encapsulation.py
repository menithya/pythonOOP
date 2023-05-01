class Person():
    def __init__(self,name, age) -> None:
        self.name = name  # public attribute
        self.age = age    # public attribute

p = Person("hello",30)
print(p.name)


# Protected  example
class Person():
    def __init__(self, name) -> None:
        self._name = name  # _ indicates protected

class Student(Person):
    def __init__(self, name, student_id) -> None:
        super().__init__(name)
        self.student_id = student_id

student = Student("nithya",11111)
print(student._name)


class Person:
    def __init__(self, name):
        self.__name = name  # private attribute

    def get_name(self):
        return self.__name

p = Person("John")
print(p.get_name())  # accessing private attribute using getter method
print(p.__name)  # throws AttributeError because the attribute is name-mangled


# Private method
class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
  def __private_method(self):
    return "I am a private method"
    
obj = PrivateClass()
print(obj.__private_method())
