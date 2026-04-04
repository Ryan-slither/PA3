def print_solution(M: list[list[int]]):
    for lst in M:
        print(lst)


def hvlcs(a: str, b: str, v: dict[str, int]) -> tuple[str, int]:
    M = []
    S: str = ""

    for i in range(len(a) + 1):
        b_row = []
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                b_row.append(0)
            else:
                b_row.append(-1)

        M.append(b_row)

    def OPT(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0

        if M[i][j] == -1:
            if a[i - 1] != b[j - 1]:
                M[i][j] = max(OPT(i - 1, j), OPT(i, j - 1))
            else:
                M[i][j] = v[a[i - 1]] + OPT(i - 1, j - 1)

        return M[i][j]

    val = OPT(len(a), len(b))

    def FindSol(i: int, j: int):
        nonlocal S
        if i == 0 or j == 0:
            return

        if a[i - 1] != b[j - 1]:
            if M[i - 1][j] >= M[i][j - 1]:
                FindSol(i - 1, j)
            else:
                FindSol(i, j - 1)
        else:
            S += a[i - 1]
            FindSol(i - 1, j - 1)

    FindSol(len(a), len(b))

    return (S[::-1], val)


if __name__ == "__main__":
    import sys
    from io_handler import parse_input, write_output

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            a, b, values = parse_input(f)
    else:
        a, b, values = parse_input()

    subseq, val = hvlcs(a, b, values)
    write_output(val, subseq)
