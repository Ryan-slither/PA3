import subprocess
import pathlib

REPO_ROOT = pathlib.Path(__file__).parent.parent
SRC = REPO_ROOT / "src" / "main.py"
DATA = REPO_ROOT / "data"


def value_of(subseq, values):
    return sum(values[c] for c in subseq)


def parse_input(input_file):
    lines = input_file.read_text().splitlines()
    k = int(lines[0])
    values = {parts[0]: int(parts[1]) for line in lines[1:k+1] for parts in [line.split()]}
    return values


def run_test(name):
    in_file = DATA / f"{name}.in"
    out_file = DATA / f"{name}.out"

    result = subprocess.run(["python3", str(SRC), str(in_file)], capture_output=True, text=True)
    got_val = int(result.stdout.strip().splitlines()[0])
    got_subseq = result.stdout.strip().splitlines()[1]

    expected_val = int(out_file.read_text().strip().splitlines()[0])
    values = parse_input(in_file)

    passed = got_val == expected_val and value_of(got_subseq, values) == expected_val
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}: value={got_val}, subsequence='{got_subseq}'")


if __name__ == "__main__":
    test_files = sorted(DATA.glob("*.in"))
    for f in test_files:
        run_test(f.stem)
