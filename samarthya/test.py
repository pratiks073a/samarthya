class person:
    def __init__(car,brand,colour):
       car.brand=brand
       car.colour=colour

    def myfunc(car):
        print(f"hello the name of the car is {car.brand} and the colour is {car.colour}")

    def __str__(car):    
        return"brand:"+ car.brand +",colour:"+str(car.colour)

p1 = person("BMW","red")
p1.myfunc()
print(p1.brand)
print(p1.colour)