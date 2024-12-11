class Animal:
    def speak(self):
        print ("animal speaking")
class Dog(Animal):
    def bark(self):
        print ("dog backing")
d = Dog()                 
d.bark()
d.speak()