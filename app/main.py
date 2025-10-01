class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{Name: " + str(self.name) + ", Health: " + str(
            self.health) + ", Hidden: " + str(self.hidden) + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if (isinstance(target, Carnivore) or not isinstance
                (target, Herbivore) or target.hidden):
            return
        target.health -= 50
        if target.health <= 0:
            Animal.alive.remove(target)
