#!/usr/bin/env python3

class Plant:
    """ A model representing a plant that can grow and update age dynamically """

    def __init__(self, name: str, height: float, age: int, growth_rate: float) -> None:
        self.name = name
        self.height = float(height)
        self.age = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def update_age(self) -> None:
        self.age += 1

    def show(self) -> str:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30, 0.8)
    rose.show()

    initial_height = rose.height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.update_age()
        rose.show()

    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")
