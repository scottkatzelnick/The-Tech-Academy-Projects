# The Tech Academy - Software Developer BootCamp
#
# Python Version: 3.8.3
#
# Author: Scott Katzelnick
#
# Purpose:
#
# POLYMORPHISM ASSIGNMENT
# Create two classes that inherit from another class.
#
# 1. Each child should have at least two of their own attributes.
#
# 2. The parent class should have at least one method (function).
#
# 3. Both child classes should utilize polymorphism on the parent class method.
#
# 4. Upload code to GitHub for review


# Parent Class - Mammals
class Mammals:
    def __init__(self, species, vertebrate, invertebrate, movement, sex):
        self.sname = species
        self.vtype = vertebrate
        self.invtype = invertebrate
        self.move = movement
        self.sextype = sex

    # Parent class method
    def get_info(self):
        print(
            "\nSpecies: {}\nVertebrate: {}\nInvertebrate: {}\nMovement Type: {}\nSex: {}".format(
                self.sname, self.vtype, self.invtype, self.move, self.sextype
            )
        )


# First child class of Mammals - Humans
class Humans(Mammals):
    def __init__(
        self, species, vertebrate, invertebrate, movement, sex, name, age
    ):
        super().__init__(species, vertebrate, invertebrate, movement, sex)
        self.fname = name
        self.humanage = age

    # Overrides parent method get_info() with polymorphism
    def get_info(self):
        print(
            "\nName: {}\nAge: {}\nSpecies: {}\nVertebrate: {}\nInvertebrate: {}\nMovement Type: {}\nSex: {}".format(
                self.fname,
                self.humanage,
                self.sname,
                self.vtype,
                self.invtype,
                self.move,
                self.sextype,
            )
        )


# Second child class of Mammals - Bear
class Bears(Mammals):
    def __init__(
        self, species, vertebrate, invertebrate, movement, sex, color, habitat
    ):
        super().__init__(species, vertebrate, invertebrate, movement, sex)
        self.bcolor = color
        self.bhabitat = habitat

    # Overrides parent method get_info() with polymorphism
    def get_info(self):
        print(
            "\nSpecies: {}\nVertebrate: {}\nInvertebrate: {}\nMovement Type: {}\nSex: {}\nColor: {}\nHabitat: {}".format(
                self.sname,
                self.vtype,
                self.invtype,
                self.move,
                self.sextype,
                self.bcolor,
                self.bhabitat,
            )
        )


if __name__ == "__main__":
    mam = Mammals(
        "Balaenoptera musculus/Blue Whale",
        True,
        False,
        "Pectoral Flippers",
        "Male",
    )
    mam.get_info()

    hum = Humans(
        "Homo sapiens/Human", True, False, "Bipedal", "Female", "Nicole", 24
    )
    hum.get_info()

    bear = Bears(
        "Ursus arctos/Brown Bear",
        True,
        False,
        "Quadrupedal",
        "Male",
        "Dark Brown",
        "Mountain Woodlands",
    )
    bear.get_info()
