# Super and __ _init_ __ methods in inheritance
## __ _init_ __
In Python __ _init_ __ is nothing but a constructor, which is called when we instantiate object.  In python we use __ _init_ __ method to initialise instance variables. This method will automatically called to initialize variables. Please note child class automatically inherit the __ _init_ __ method if not defined in child class.
## Super method 
Super keyword is used to call parent class method, including __ _init_ __ method of parent class

 
By taking below samples, we will study  following usecases
- what will happen if child class does not going to have __ init __  method 
- what will happen if child class has it's own __ init__  method
- what will happen if child class does not calls super method
- What will happen if child class calls super method

##  what will happen if child class does not going to have __ init __  method  deifined in it



# isinstance and issubclass
isinstacne and issublcass are built-in funciton of python used to determine type of given varaible.

isinstance(object, classinfo) function takes an object and a class or a tuple of classes as input and returns True if the object is an instance of the class or any of the classes in the tuple. Otherwise, it returns False.

# Extending and overrrid
Extending a class means adding new attributes or methods to the child class

Overriding a method means to inherit a method from the parent class, keep its name, but change the contents of the method.

Overriding deals with changing a pre-existing method from the parent class, while extending deals with adding new methods and attributes.

# Multiple Inheritance
# Overriding the __init__ Method in multiple Ineheritance

When a class inherits from multiple parent classes that have their own __init__ methods, the subclass can override the __init__ method of one or more of its parent classes to customize the initialization process for the subclass.

In single level inhertance just calling super().__init__() will pass data in parent class. Where as in Multiple level inheritance this does not works, becuase super().__init__()  does not which parent class method to call. Solution can be found. Even expeclity calling __init__ method like this also creates error

```
class Tyrannosaurus(Dinosaur, Carnivore):
  def __init__(self, size, weight, diet):
    super().__init__(size, weight)
    super().__init__(diet)
````
Python does not know if super() is referring to the Dinosaur class or the Carnivore class. Overriding the __init__ method for multiple inheritance requires a unique structure. Instead of super() use the name of the class. You must also pass self to the parent __init__ method.

[Mutliple Inheritance](MultipleInheritance.py)

# how does isinstance and issubclass works in multiple inheritance

# Encpsulation
Encapsulation is a fundamental concept in object-oriented programming that refers to the practice of hiding the internal implementation details of an object from the outside world and providing a well-defined interface for interacting with the object.

Encapsulation is a concept in which related data and methods are grouped together, and in which access to data is restricted.

**Note**: Python does not use the **public** and **private** keywords

# Public, Protected and Private
**Public attributes**: These are attributes that can be accessed from anywhere, both inside and outside the class. In Python, all attributes and methods that do not have a leading underscore or double underscore are considered public. Here is an example:

[public-Encapsulation](Encapsulation.py)

**Protected attributes**: These are attributes that are intended to be accessed only within the class or by subclasses. **In Python, attributes with a single leading underscore are considered protected**. This convention serves as a hint to other developers that the attribute should not be accessed from outside the class. However, it is still technically possible to access the attribute from outside the class. Here is an example:

[Protected-Encapsulation](Encapsulation.py)

**Private attributes**: These are attributes that are intended to be accessed only within the class. In Python, attributes with a double leading underscore are considered private. This naming convention causes the attribute to be "name-mangled" by the interpreter, which means that its name is modified to include the class name to prevent accidental access from outside the class. Here is an example:

[Private-Encapsulation](Encapsulation.py)

## Name mangling
``` 
class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
obj = PrivateClass()
print(obj._PrivateClass__private_attribute)
```
When the Python interpreter encounters an attribute with a double underscore, it does not make it private. Instead, it changes the name to _ClassName__AttributeName. That is why Python returns and error for print(obj.__private_attribute). __private_attribute does not exist. It has been renamed to _PrivateClass__private_attribute. This whole process is called name mangling, and it is designed to avoid name collisions in inheritance. Name mangling, however, gives the appearance of private attributes and methods







