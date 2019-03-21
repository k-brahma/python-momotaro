class Creature:
    def __init__(self, typename):
        self.typename = typename

    def gettype(self):
        return self.typename


class Animal(Creature):
    def __init__(self, typename):
        super().__init__(typename)


class Human(Animal):
    def __init__(self, typename):
        super().__init__(typename)


class Oni(Creature):
    def __init__(self, typename):
        super().__init__(typename)
