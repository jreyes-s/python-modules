#!/usr/bin/env python3

import sys


def ft_score_analytics(score: list[int]) -> None:
    total_players = len(score)
    total_score = sum(score)
    average_score = total_score / total_players
    high_score = max(score)
    low_score = min(score)
    score_range = high_score - low_score

    print(f"Scores processed: {score}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")
    print()


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        print()
        sys.exit(1)

    clean_scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            clean_scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not clean_scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        print()
    else:
        ft_score_analytics(clean_scores)
