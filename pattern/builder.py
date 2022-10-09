"""
*What is this pattern about?
It decouples the creation of a complex object and its representation,
so that the same process can be reused to build objects from the same
family.
This is useful when you must separate the specification of an object
from its actual representation (generally for abstraction).
"""

# Abstract Building
class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big"


class Flat(Building):
    def build_floor(self):
        self.floor = "More than One"

    def build_size(self):
        self.size = "Small"


# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)


class ComplexBuilding:
    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big and fancy"


def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


def main():
    """
    >>> house = House()
    >>> house
    Floor: One | Size: Big

    >>> flat = Flat()
    >>> flat
    Floor: More than One | Size: Small

    # Using an external constructor function:
    >>> complex_house = construct_building(ComplexHouse)
    >>> complex_house
    Floor: One | Size: Big and fancy
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()