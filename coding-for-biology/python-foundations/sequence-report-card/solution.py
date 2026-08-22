import sys


def solve(identifier: str, seq: str) -> None:
    # Write your solution here.
    # Print three labelled lines reporting the identifier, sequence length, and first base to stdout.
    print(f"ID: {identifier}")
    print(f"Length: {len(seq)}")
    print(f"First base: {seq[0]}")


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    identifier = data[0].strip()  # The sequence identifier
    seq = data[1].strip()  # The DNA sequence
    solve(identifier, seq)