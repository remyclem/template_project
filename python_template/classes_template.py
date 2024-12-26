# codding: utf-8
"""
Template for creating classes.
"""

class Character:

    def __init__(self, name, hp, team_name=None, origin_story=None):
        self._name = name  # starts with "_" because it is meant to be protected
        self._hp = hp
        self.__team_name = team_name
        self.__origin_story = origin_story  # starts with "__" because it is meant to be private

    @property
    def name(self):
        return self._name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    @property
    def hp(self):
        return self._hp

    def get_hp(self):
        return self._hp

    def set_hp(self, value):
        self._hp = value

    def show(self):
        print("- Name : {}".format(self._name))
        print("- HP : {}".format(self._hp))


class Warrior(Character):

    character_class = "WARRIOR"  # class attribute

    def __init__(self, name, hp):
        super().__init__(name, hp)


class Wizard(Character):

    character_class = "WIZARD"  # class variable

    def __init__(self, name, hp, school_of_magic):
        super().__init__(name, hp)
        self.school_of_magic = school_of_magic

    def show(self):
        super().show()
        print("- School of magic : {}".format(self.school_of_magic))


if __name__ == "__main__":

    Kratos = Warrior("Kratos", 30)
    Kratos.show()

    print(Kratos.get_hp())
    print(Kratos.hp)

    Gandalf = Wizard("Gandalf", 20, "Grey Magic")
    Gandalf.show()
    print(" - " + Gandalf.character_class)
    del(Gandalf)
    print(" - " + Wizard.character_class)