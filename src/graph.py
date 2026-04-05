from time import perf_counter

import matplotlib.pyplot as plt

from generator import generate_input
from main import hvlcs


def graph_hvlcs(min_sequence_length: int, max_sequence_length: int):
    """Generates inputs of length min_sequence_length to max_sequence_length and graphs the running time of each. Use with big values for the best representation of running time"""
    times = []

    for n in range(min_sequence_length, max_sequence_length):
        A, B, vals = generate_input(10, n, n, 10)

        total_time = 0
        runs = 3
        for _ in range(runs):
            start_a = perf_counter()
            hvlcs(A, B, vals)
            end_a = perf_counter()
            total_time += end_a - start_a

        avg_time = total_time / runs
        times.append(avg_time)
        print(f"Length: {n}  Time: {avg_time}", end="\r")

    plt.plot(
        list(range(min_sequence_length, max_sequence_length)),
        times,
        marker="o",
        label="HVLCS",
    )

    plt.xlabel("n (length of subsequences)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime of HVLCS Algorithm vs. n")
    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    graph_hvlcs(1, 600)
