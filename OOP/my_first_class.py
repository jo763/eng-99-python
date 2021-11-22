class Dog:
    animal_kind = "canine" # class variable

    def __init__(self): # Initialise, something that occurs when the instance is created. dunder is phonetically used to underscore underscore
        self.legs = 4



    def bark(self):
        return "Woof!"

print(Dog.animal_kind)
fido = Dog()
print(fido.animal_kind)
print(fido.bark())[p]