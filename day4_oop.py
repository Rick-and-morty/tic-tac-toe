
class Person:

    def __init__(self, name):
        self.name = name


class Bike:

    def __init__(self, speeds, owner):
        self.speed = speeds
        self.owner = owner
        self.color = "grey"
        self._layers = 1

    def set_color(self, new_color):
        self._layers += 1
        self.color = new_color

    def get_layers(self):
        return self.layers

tyler = Person("tyler")
joel = Person("joel")
bike = Bike(100, joel)
tylers_bike = Bike(18, tyler)

print("OWNERS===========")
print(bike.owner.name)
print(tylers_bike.owner.name)

print("color before we change it")
print(bike.color)
print(bike.speed)
print(bike.get_layers)

print("color after we change it")
bike.set_color("midnight blue")
print(bike.color)
print(bike.get_layers)

print("color of tylers bike")
print(tylers_bike.color)
