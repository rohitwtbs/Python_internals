# The circle should have a radius, a diameter, and an area. It should also have a nice string representation
#  make sure when the radius of your class changes that the diameter and area both change as well:
# make sure you can set the diameter attribute in your class and the radius will update accordingly.
#  Also make sure also that you cannot set the area (setting area should raise an AttributeError):
# make sure your radius cannot be set to a negative number.
# You should raise a ValueError exception with the error message 
# Radius cannot be negative (yes the tests check for the error message).


class Circle:
    def __init__(self,radius=1):
        self.radius = radius
    @property
    def daimeter(self):
        return self.radius * 2
    @property
    def area(self):
        return 3.14 * self.radius * self.radius
    

obj_c = Circle(5)
# print(obj_c.radius)
print(obj_c.daimeter)
print(obj_c.area)