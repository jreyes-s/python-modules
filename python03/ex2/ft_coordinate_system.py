#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        tp = []
        for part in parts:
            try:
                tp.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                break
        else:
            return tuple(tp)


def main() -> None:
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x1, y1, z1 = pos1
    distance1 = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {distance1}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    distance2 = round(
        math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance2}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    main()
