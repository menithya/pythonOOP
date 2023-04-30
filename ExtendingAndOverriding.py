class Person:
    def __init__(self,name,age,occupation) -> None:
        self.name = name
        self.age = age
        self.occupation = occupation

    def get_name(self):
        print(f"Hey my name is {self.name}")
    
    def get_age(self):
        print(f"Hello this perron {self.name} is {self.age}")


class Superhero(Person):
    def __init__(self, name, age, occupation,ssn) -> None:  # example of overriding
        super().__init__(name, age, occupation)
        self.ssn = ssn

    def get_name(self):  # Overriding get_name method in child class
         print(f"Hey my name is from child class {self.name}")

    def get_ssn(self):  # Example of extending
        print(f"My ssn number is {self.ssn}")



hero = Superhero("nithya",30, "Lead",111)
hero.get_name()  #output nithya

print(help(Superhero))