# /usr/bin/env python3

import random


def main() -> None:
    players_list: list[str] = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]

    new_lst_cap = [player.capitalize() for player in players_list]

    cap_list_only_old = [
        player for player in players_list if player == player.capitalize()
    ]

    score_dict = {
        player: random.randint(0, 999) for player in players_list
    }

    print(f"Initial list of players: {players_list}")
    print(f"New list with all names capitalized: {new_lst_cap}")
    print(f"New list of capitalized names only: {cap_list_only_old}")
    print(f"Score dict: {score_dict}")

    score_average = round(
        sum(score_dict.values()) / len(new_lst_cap), 2
    )
    print(f"Score average is {score_average}")

    high_score = {
        player: score_dict[player]
        for player in score_dict if score_dict[player] > score_average
    }
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    main()
