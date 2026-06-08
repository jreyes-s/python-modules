#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age
        print(
            f"Plant created: {self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old")

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(
            f"Current state: {self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)

    print()
    rose.set_height(25)
    rose.set_age(30)

    print()
    rose.set_height(-22225.0)
    rose.set_age(-300)

    print()
    rose.show()
