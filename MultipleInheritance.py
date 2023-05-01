class Dinosaur:
  def __init__(self, size, weight):
    self.size = size
    self.weight = weight
    
class Carnivore:
  def __init__(self, diet):
    self.diet = diet
    
class Tyrannosaurus(Dinosaur, Carnivore):
  def __init__(self, size, weight, diet):
    Dinosaur.__init__(self, size, weight) # please note we are passing self
    Carnivore.__init__(self, diet)
    
tiny = Tyrannosaurus(12, 14, "whatever it wants")


class Human:
  def __init__(self, name,age) -> None:
    self.name = name
    self.age = age

class Artist:
  def __init__(self, style) -> None:
    self.style = style

class Art_Student(Human,Artist):
  def __init__(self, name, age,style) -> None:
    Human.__init__(self,name, age)  # self is passed
    Artist.__init__(self,style)

student = Art_Student("Roberta", 19, "cubism")
print(student.name)
print(student.age)
print(student.style)


# isinstance and issublcass
class A:
  pass

class B:
  pass

class C:
  pass

class D(A, B):
  pass

obj= D()
print(isinstance(obj, D))
print(issubclass(D, A))
print(isinstance(obj, A))
print(issubclass(D, B))
print(issubclass(D, C))


