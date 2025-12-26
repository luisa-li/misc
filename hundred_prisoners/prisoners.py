"""A simulation of the prisoners dilemma problem."""

import pickle
import random

from matplotlib import pyplot as plt
from tqdm import tqdm


def permutation_cycles(n):

    perm = list(range(1, n + 1))
    random.shuffle(perm)

    visited = [False] * (n + 1)
    longest_cycle = 0

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            current = i

            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = perm[current - 1]

            if len(cycle) > longest_cycle:
                longest_cycle = len(cycle)

    return longest_cycle


def simulate_prisoners(n: int, trials: int):
    return [permutation_cycles(n) for _ in range(trials)]


if __name__ == "__main__":

    combined_longest_cycles = []
    for i in tqdm(range(0, 1000)):
        longest_cycles = simulate_prisoners(i, 10000)
        combined_longest_cycles.append(longest_cycles)

    with open("combined_longest_cycles.pkl", "wb") as f:
        pickle.dump(combined_longest_cycles, f)