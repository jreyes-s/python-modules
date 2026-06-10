#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    arguments: list[str] = sys.argv[1:]
    inventory: dict[str, int] = dict()

    """ Check if arg contains ':' """
    for argument in arguments:
        if ":" not in argument or argument[-1] == ":":
            print(f"Error - invalid parameter '{argument}'")
            continue

        item_name, text_quantity = argument.split(":", 1)

        """ Check for duplicates """
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(text_quantity)
            inventory[item_name] = quantity
        except ValueError as error:
            print(f"Quantity error for '{text_quantity}': {error}")
            continue
    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_items = len(inventory)
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {total_items} items: {total_quantity}")

    most_abundant_item, most_abundant_qty = max(
        inventory.items(), key=lambda x: x[1])
    least_abundant_item, least_abundant_qty = min(
        inventory.items(), key=lambda x: x[1])

    for item in item_list:
        qty = inventory[item]
        percentage = (qty / total_quantity *
                      100) if total_quantity > 0 else 0.0
        print(f"Item {item} represents {round(percentage, 1)}%")

    print(
        f"Item most abundant: {most_abundant_item} with quantity "
        f"{most_abundant_qty}")
    print(
        f"Item least abundant: {least_abundant_item} with quantity "
        f"{least_abundant_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
