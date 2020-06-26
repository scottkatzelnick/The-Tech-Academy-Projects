# Parent Class
class Organism:
    name: str = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(
            self.name,
            self.species,
            self.legs,
            self.arms,
            self.dna,
            self.origin,
            self.carbon_based,
        )
        return msg


# Child class instance
class Human(Organism):
    name = "MacGuyver"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    @staticmethod
    def ingenuity():
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum and a roll of duct tape!"
        return msg


# Another child class instance
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    @staticmethod
    def intimidate():
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg


# Another child class instance
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    @staticmethod
    def replication():
        msg = "\nThe cells begin to divide and multiply into two separate organisms!"
        return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.intimidate())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
