##inheritance  allows a class (child )to inherit props and methods  of a parent class
class Animals:

    def init(self, name):

        self.name = name

    def Speak(self):

        return f'Animal name {self.name} makes a sound'

class Dog(Animals):

    def init(self, name, breed):

        super().init(name)

        self.breed = breed

    def Speak(self):
        return f'{self.name} barks ...'

# instances ...
dog1 = Dog('Scubby Doo!', 'Generic')

animal1 = Animals('Generic Animals')

print
print (animal1.Speak())
print(dog1.Speak())

# Example 2 ...
# class Laptop:

#     def init(self, name, screen_size):

#         self.name = name
#         self.screen_size = screen_size

#     def str(self):
#         return f'Laptop name : {self.name}. . Sreen SIze : {self.screen_size}'

# class HP(Laptop):
#     def init(self,name, screen_size, color, model):
#         super().init(name, screen_size)
#         self.color = color
#         self.model = model

#     def str(self):
#         return f'Laptop name: {self.name}, laptop Screen-size: {self.screen_size}, Laptop color: {self.color}. . laptop model : {self.model}'

# class Dell(Laptop):

#     def init(self, name, screen_size, storage, RAM):
#         super().init(name, screen_size)

#         self.storage = storage
#         self.Ram = RAM
#     def str(self):
#         return f'Laptop name: {self.name}, Lapotop screen-size : {self.screen_size}, laptop Storage : {self.storage}, and the RAM : {self.Ram}'

# # instance
# hp1 = HP('Elite-book', "13.2''", 'Black-grey', 'Core i5')

# dell10 = Dell('Ricky',"17.1''", '250gb', '8gb RAM')

# print(hp1)
# print(dell10)


