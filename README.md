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

# The Property Class
The property class in Python allows the programmer to use getters and setters in a pythonic way. There are two ways to implement the property class. One way is with the @property decorator, and the second way is with the property function. Both implementations do the same thing, and there is no difference in how the user would interact with the class. There is a slight difference in how the code is written. The @property decorator will be introduced first.

# Polymorphism

Polymorphism is the ability of an object to take on different forms. In object-oriented programming, polymorphism is often achieved through inheritance and method overriding.

Polymorphism can be of two types: compile-time polymorphism and runtime polymorphism.

Compile-time polymorphism, also called method overloading, occurs when multiple methods in a class have the same name but different parameters. The compiler determines which method to call based on the number and types of the arguments provided.

Runtime polymorphism, also called method overriding, occurs when a subclass provides its own implementation of a method that is already defined in its superclass. When an object of the subclass is used to call the method, the subclass implementation is called instead of the superclass implementation.

Polymorphism allows for code reuse and makes code more flexible and adaptable to different situations. It also allows for code to be written in a more general way, without the need for specific implementations for every possible scenario.
## Method Overloading
Method overloading is another example of polymorphism. Method overloading occurs when you have a single method name that can take different sets of parameters. Imagine you want to write the method sum that can sum up to three numbers. The math involved with three parameters is slightly different that two parameters, which is different from 1 parameter, etc. Traditionally, if you declare a method that takes three parameters but only pass two, Python will throw an error message. Instead let’s create a class that has two sum methods; one with two parameters and another with three parameters.

```
class TestClass:
  def sum(self, a, b, c):
    return a + b + c
  
  def sum(self, a, b):
    return a + b
  
obj = TestClass()
print(obj.sum(1, 2))
print(obj.sum(1, 2, 3)) // this will through error
```

**Note** When two or more methods have the same name, Python only recognizes the last method. All of the others are ignored. That is why you got an error message. Python only recognizes the second sum method.

## Operator Overloading

```
class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __add__(self, other):
    return self.account + other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments + my_banking)
```


## Magic Methods

```
-	object.__sub__(self, other)
*	object.__mul__(self, other)
/	object.__truediv__(self, other)
//	object.__floordiv__(self, other)
<	object.__lt__(self, other)
<=	object.__le__(self, other)
==	object.__eq__(self, other)
!=	object.__ne__(self, other)
>	object.__gt__(self, other)
>=	object.__ge__(self, other)
```

# Duck typing
Duck typing is a concept in Python (and some other programming languages) where the type or class of an object is less important than its behavior. The idea is that if an object walks like a duck, quacks like a duck, and swims like a duck, then it can be treated like a duck, regardless of its actual type.

In other words, in duck typing, the interpreter does not check the type of an object when it is used, but rather it checks whether the object has the required attributes or methods to perform a specific operation.

Here is an example to illustrate duck typing in Python:
```
class Duck:
    def quack(self):
        print("Quack, quack!")
    
    def swim(self):
        print("Swimming...")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")
    
    def swim(self):
        print("I'm swimming like a duck!")

def make_it_quack_and_swim(obj):
    obj.quack()
    obj.swim()

# create a Duck object
duck = Duck()

# create a Person object
person = Person()

# pass the Duck object to the function
make_it_quack_and_swim(duck) # prints "Quack, quack!" and "Swimming..."

# pass the Person object to the function
make_it_quack_and_swim(person) # prints "I'm quacking like a duck!" and "I'm swimming like a duck!"

```

In this example, we define a Duck class and a Person class, both of which have quack and swim methods. We then define a function make_it_quack_and_swim that takes an object and calls its quack and swim methods.

We create a Duck object and a Person object, and then pass each of them to the make_it_quack_and_swim function. Because both objects have quack and swim methods, they can be treated like ducks, and the function works correctly for both objects.

This example demonstrates how duck typing allows Python code to be more flexible and adaptable to different situations. By focusing on the behavior of an object rather than its type, Python code can work with a wide variety of objects without the need for explicit type checking or casting.


# Composition
[Composition-Example](Composition.py)
## Composition versus Inheritance **

Assume you have the class MyClass. You want to use this class in your program, but it is missing some functionality. Do you use inheritance and extend the parent class, or do you use composition and create a component class? Both of these techniques can accomplish the same thing. This is a complex topic, but you can use a simple test to help you decide. 

**Use inheritance if there is an “is a” relationship, and use composition if there is a “has a” relationship.**


For example, you have the Vehicle class and you want to make a Car class. Ask yourself if a car has a vehicle or if a car is a vehicle. A car is a vehicle; therefore you should use inheritance. Now imagine that you have a Phone class and you want to represent an app for the phone. Ask yourself if a phone is an app or if a phone has an app. A phone has an app; therefore you should use composition.







