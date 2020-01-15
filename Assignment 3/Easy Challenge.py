# Inheritance is a powerful feature in object oriented programming.
#
# It refers to defining a new class with little or no modification to an existing class.
# The new class is called derived (or child) class and
# the one from which it inherits is called the base (or parent) class.

# Simple example of the power of inheritence.


class Humanoid:
    def __init__(self):
        self.hp = 100
        self.intellect = 10
        self.stamina = 5


class Human(Humanoid):
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction
        self.sword_skill = 10


class HumanChildren(Humanoid):
    def __init__(self, age, father, mother):
        self.age = age
        self.father = father
        self.mother = mother


class Ogre(Humanoid):
    def __init__(self, faction):
        self.faction = faction
        self.strength = 10

class Elf(Humanoid):
    def __init__(self):
        self.wisdom = 10

class HalfElf(Elf, Human):
    def __init__(self):
        self.endurance = 10

class ElfChildren(Elf):
    def __init__(self, age, father, mother):
        self.age = age
        self.father = father
        self.mother = mother
