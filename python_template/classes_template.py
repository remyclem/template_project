# codding: utf-8
"""
Template for creating classes.
"""

class Character:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def show(self):
        print("- Name : {}".format(self.name))
        print("- HP : {}".format(self.hp))

    def save_as_file(self):  # TODO
        pass

    def load_from_file(self):  # TODO
        pass


class Warrior(Character):

    character_class = "WARRIOR"  # class attribute

    def __init__(self, name, hp):
        super().__init__(name, hp)


class Wizard(Character):

    character_class = "WIZARD"

    def __init__(self, name, hp, school_of_magic):
        super().__init__(name, hp)
        self.school_of_magic = school_of_magic

    def show(self):
        super().show()
        print("- School of magic : {}".format(self.school_of_magic))


if __name__ == "__main__":

    Kratos = Warrior("Kratos", 30)
    Kratos.show()
    print(" - " + Kratos.character_class)

    Gandalf = Wizard("Gandalf", 20, "Grey Magic")
    Gandalf.show()
    print(" - " + Wizard.character_class)