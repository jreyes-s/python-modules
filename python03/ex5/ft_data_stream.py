#!/usr/bin/env python3

from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    """An endless generator picking a random player and action."""
    players: list[str] = [
        "alice",
        "bob",
        "charlie",
        "dylan"
    ]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use"
    ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(lista: list) -> Generator[tuple[str, str], None, None]:
    while lista:
        idx = random.randrange(len(lista))
        event = lista.pop(idx)
        print(f"Got event from list: {event}")
        yield event


if __name__ == "__main__":
    events = gen_event()

    for i in range(1000):
        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = [next(events) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for _ in consume_event(event_list):
        print(f"Remains in list: {event_list}")
