#!/usr/bin/env python3


class Plant:
    """A model representing a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """ Display the plants information in a single organized line """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    garden = [rose, sunflower, cactus]

    for plant in garden:
        plant.show()
