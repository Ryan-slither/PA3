import sys


def parse_input(source=None) -> tuple[str, str, dict[str, int]]:
    """
    Parse HVLCS input from a file object or stdin.

    Format:
        K
        x1 v1
        x2 v2
        ...
        xK vK
        A
        B
    """
    if source is None:
        source = sys.stdin

    lines = [line.rstrip("\n") for line in source.readlines()]
    i = 0

    k = int(lines[i]); i += 1

    values: dict[str, int] = {}
    for _ in range(k):
        char, val = lines[i].split(); i += 1
        values[char] = int(val)

    a = lines[i]; i += 1
    b = lines[i]; i += 1

    return a, b, values


def write_output(value: int, subsequence: str, dest=None) -> None:
    """Print the maximum value and the optimal subsequence."""
    if dest is None:
        dest = sys.stdout

    dest.write(f"{value}\n")
    dest.write(f"{subsequence}\n")
