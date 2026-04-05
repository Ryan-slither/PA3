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

    def OPT_rec(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0

        if M[i][j] == -1:
            if a[i - 1] != b[j - 1]:
                M[i][j] = max(OPT_rec(i - 1, j), OPT_rec(i, j - 1))
            else:
                M[i][j] = v[a[i - 1]] + OPT_rec(i - 1, j - 1)

        return M[i][j]

    def OPT_iter() -> int:
        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                if a[i - 1] != b[j - 1]:
                    if M[i - 1][j] >= M[i][j - 1]:
                        M[i][j] = M[i - 1][j]
                    else:
                        M[i][j] = M[i][j - 1]
                else:
                    M[i][j] = v[a[i - 1]] + M[i - 1][j - 1]

        return M[len(a)][len(b)]

    # val = OPT_rec(len(a), len(b))
    val = OPT_iter()

    def FindSolRec(i: int, j: int):
        nonlocal S
        if i == 0 or j == 0:
            return

        if a[i - 1] != b[j - 1]:
            if M[i - 1][j] >= M[i][j - 1]:
                FindSolRec(i - 1, j)
            else:
                FindSolRec(i, j - 1)
        else:
            S += a[i - 1]
            FindSolRec(i - 1, j - 1)

    def FindSolIter():
        nonlocal S
        i = len(a)
        j = len(b)
        while i > 0 and j > 0:
            if a[i - 1] != b[j - 1]:
                if M[i - 1][j] >= M[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
            else:
                S += a[i - 1]
                i -= 1
                j -= 1

    # FindSolRec(len(a), len(b))
    FindSolIter()

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
