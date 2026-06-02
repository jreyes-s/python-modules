#!/usr/bin/env python3

class Plant:
    """ A model representing a plant, initialized inmediately upon construction """

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def show(self) -> None:
        """ Displays the plant's information """
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("== Plant Factory Output ===")

    garden_factory = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    for plant in garden_factory:
        plant.show()
