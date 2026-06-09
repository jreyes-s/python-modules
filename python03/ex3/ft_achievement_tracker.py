#!/usr/bin/env python3

import random

ACHIEVEMENT_POOL = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable', 'Speed Runner',
    'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
]


def gen_player_achievements() -> set:
    num_achievements = random.randint(5, 9)
    chosen = random.sample(ACHIEVEMENT_POOL, num_achievements)

    return (set(chosen))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        'Alice': gen_player_achievements(),
        'Bob': gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan': gen_player_achievements()
    }

    for player, achiev_func in players.items():
        print(f"Player {player}: {achiev_func}")

    all_distinct = set()
    for achievements in players.values():
        all_distinct = set.union(all_distinct, achievements)
    print(f"All distinct achievements: {all_distinct}")

    common = players['Alice']
    for achievements in players.values():
        common = set.intersection(common, achievements)
    print(f"Common achievements: {common}")

    for name, achievements in players.items():
        everyone_else = set()
        for other_name, other_achievements in players.items():
            if name != other_name:
                everyone_else = set.union(everyone_else, other_achievements)
        unique_players = achievements - everyone_else
        print(f"Only {name} has: {unique_players}")

    full_pool_set = set(ACHIEVEMENT_POOL)
    for name, achievements in players.items():
        missing = set.difference(full_pool_set, achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
