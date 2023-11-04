class Animal: 
    def __init__(self,name):
        self.name = name 
    
    def speak(self):
        return f'{self.name} says Animal'
    
    def reply(self):
        return f'{self.name} says Meow!'
         
class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        return f'{self.name} says Mammal!'

class Cat(Mammal): 
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        self.reply()
        return f'{self.name} says Meow!'

class Dog(Mammal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return f'{self.name} says Bark'
    
class Primate(Mammal):
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        return f'{self.name} says Primate!'

class ComputerScientist(Primate):
    def __init__(self,name):
        super().__init__(name)
   
