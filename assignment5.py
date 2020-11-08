
class animal():
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes

class wild_animals(animal):
    def place(self):
        print("Lives in forest")
        
class carnivores(wild_animals):
    def food(self):
        print("Eats meat")
        
class bear(carnivores):
    def sound(self):
        print("growls")
    def colour(self):
        print("It's colour is orange with black stripes")
    def young_ones(self):
        print("IT's young one is called as cub")
    
class tiger(carnivores):
    def sound(self):
        print("roars")
    def colour(self):
        print("It's colour is yellow")
    def young_ones(self):
        print("It's young one is called as cub")
        
        
class herbivores(wild_animals):
    def food(self):
        print("Eats grass and fruits")
        
class cow(herbivores):
    def sound(self):
        print("It moos")
    def colour(self):
        print("Many colours such as black and brown")
    def young_ones(self):
        print("It's young one is called as calf")
        
class rabbit(herbivores):
     def sound(self):
        print("It squeks or grunts")
     def colour(self):
        print("Many colours such as brown and white")
     def young_ones(self):
        print("It's young one is called as bunny")
               
class woodpeckers(herbivores):
     def sound(self):
        print("It shrills")
     def colour(self):
        print("Many colours such as black and red")
     def young_ones(self):
        print("It's young one is called as chick")

t1 = tiger();
print(t1.eyes)
print(t1.legs) 
t1.colour();
t1.young_ones();
t1.sound();
t1.food();
t1.place();       
