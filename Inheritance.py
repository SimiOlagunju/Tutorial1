#class is the collection of object. A blueprint/template that allows us to model anything in the realworld or in a software

class Car:                               # car is the object
    
    car_type ='sedan'                         #class attribute

    def __init__(self, name, mileage):   #constructormethod/parameter
        self.name = name                 #instance attribute
        self.mileage = mileage           #instance attribute
    
    def description(self):               #instance method
        return f'The {self.name} car gives the mileage of {self.mileage}km/1.'

    def max_speed(self, speed):          #instance method
        return f'The {self.name} runs at maximum speed of {speed}km/1.'

obj1 = Car('Toyota', 24.5)               #object 
print(obj1.description())                #objectname.methodname
print(obj1.max_speed(150))               #objectname.methodname


class Car:       #parent class
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f'The {self.name} car gives the mileage of {self.mileage}km/1.'
 
class A(Car):      #childclass
    pass

class B(Car):       #childclass
    def Bmw_series(self):
        return f'This is the description method of class Bmw! '

obj1 = A('Audi series 1', 30.5)
print(obj1.description())

obj2 = B('Bmw series 4', 29.7)
print(obj2.description())
print(obj2.Bmw_series())
























