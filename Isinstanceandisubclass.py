class Person:
    pass

class Student(Person):
    pass

person = Person()
student = Student()

print(isinstance(person, Person)) # True
print(isinstance(student, Student)) # True
print(isinstance(student, Person)) # True
print(isinstance(person, Student)) # False


class Person:
    pass

class Student(Person):
    pass

print(issubclass(Student, Person)) # True
print(issubclass(Person, Student)) # False
print(issubclass(Student, object)) # True



class ClassA:
  pass
    
class ClassB(ClassA):
  pass

class ClassC:
  pass

class ClassD(ClassC):
  pass

object_a = ClassA()
object_b = ClassB()
object_c = ClassC()
object_d = ClassD()

print(isinstance(object_b, ClassA))
print(isinstance(object_d, ClassC))

print(issubclass(ClassB, ClassA))
print(issubclass(ClassD, ClassC))



