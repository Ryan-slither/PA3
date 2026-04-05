import random
from pathlib import Path

from io_handler import write_input, write_output_file
from main import hvlcs

ALPHABET = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def generate_input(
    unique_chars: int, min_length: int, max_length: int, highest_score: int
) -> tuple[str, str, dict[str, int]]:
    A = ""
    B = ""
    vals: dict[str, int] = {}

    chosen_chars = random.sample(ALPHABET, min(len(ALPHABET), unique_chars))

    for c in chosen_chars:
        vals[c] = random.randint(1, highest_score)

    for _ in range(random.randint(min_length, max_length)):
        A += random.choice(chosen_chars)

    for _ in range(random.randint(min_length, max_length)):
        B += random.choice(chosen_chars)

    return (A, B, vals)


if __name__ == "__main__":
    for n in range(6, 16):
        A1, B1, vals1 = generate_input(random.randint(5, 10), 25, 35, 10)
        write_input(Path(f"./data/test{n}.in"), vals1, A1, B1)
        res, val = hvlcs(A1, B1, vals1)
        write_output_file(Path(f"./data/test{n}.out"), val, res)
