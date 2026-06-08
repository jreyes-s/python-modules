#!/usr/bin/env python3

class GardenError(Exception):
    """Exception base for the garden"""

    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """For problems with plants"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """For problems with watering"""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_problem() -> None:
    """Raises a custom PlantError"""
    raise PlantError("The tomato plant is wilting!")


def raise_water_problem() -> None:
    """Raises a custom WaterError"""
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        raise_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    for action in [raise_plant_problem, raise_water_problem]:
        try:
            action()
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")
