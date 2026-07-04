class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "..."
class Dog(Animal):
    def speak(self):
        return "woof"
class cat(Animal):
    def speak(self):
        return "Meow"
    
cheeku=Dog("Cheeku")
print(cheeku.speak())
rexi=cat("REXI")
print(rexi.speak())
gorilla=Animal("Gorilla")
print(gorilla.speak())