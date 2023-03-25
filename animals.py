class Dog:
    breed = "Labrador"
    
    def __init__(self,name):
         self.name = name
         self.woofs = 0

    def count(self):
        self.woofs += 1
        for barks in range(self.woofs):
            self.speak()

    def speak(self):
        print("Woof!")
    
    
    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")


    def hear(self,word):
        if self.name in word:
            self.speak()

class labrador(Dog):
    def speak(self):
        print("Woooof!")




class Cat:
    def __init__(self):
        self.mood = 'neutral'
    
    def speak(self):
        if self.mood == "happy":
            print("Purr")
        elif self.mood == "angry":
            print("Hiss!") 
        else:
            print("Meow!")