class Dog:   
    scien_name = "Canis lupus familiaris" #class-level variables
    
    def __init__(self,name,breed):
        self.woofs = 0 #instance variable
        self.name = name # self.name is an instance variable

    def count(self):
        self.woofs += 1 
        for bark in range(self.woofs):
            self.speak()

    def speak(self): #method
        print("Woof!")

    def eat(self,str):
        if str == "biscuit":
            print("Yummy!")
        else:
            print("That's not food for a dog!")

class Cat:
    def __init__(self):
        self.mood = 'neutral' #self.mood is an instance var
        self.breed = 'persian' #self.breed is an instance var
