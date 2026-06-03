#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def grow(self, amount: float) -> None:
        self._height += amount

    def age(self, days: int) -> None:
        self._age += days

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk: float
    ) -> None:
        super().__init__(name, height, age)

        if trunk < 0:
            print(f"{self._name}: Error, trunk diameter can't be negative")
            self._trunk = 0.0
        else:
            self._trunk = trunk

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces shade of {round(self._height, 1)}cm long and {round(self._trunk, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest: str, nutritional: int = 0) -> None:
        super().__init__(name, height, age)
        self._harvest = harvest
        self._nutritional = nutritional

    def grow(self, amount: int, nutritional_value: int) -> None:
        super().grow(amount)
        self._nutritional += nutritional_value

    def age(self, days: int) -> None:
        super().age(days)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest}")
        print(f"Nutritional value: {self._nutritional}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print(f"[make tomato grow and age for 20 days]")
    tomato.age(20)
    tomato.grow(42, 20)
    tomato.show()
