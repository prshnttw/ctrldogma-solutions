import sys


def solve(n: int, sequences: list[str]) -> None:
    length = len(sequences[0])

    # Profile matrix
    profile = {
        "A": [0] * length,
        "C": [0] * length,
        "G": [0] * length,
        "T": [0] * length
    }

    # Count bases at each position
    for sequence in sequences:
        for i, base in enumerate(sequence):
            profile[base][i] += 1

    # Build consensus
    consensus = ""

    for i in range(length):
        bases = "ACGT"
        best_base = max(
            bases,
            key=lambda base: profile[base][i]
        )
        consensus += best_base

    # Output
    print(consensus)

    for base in "ACGT":
        print(f"{base}: {' '.join(map(str, profile[base]))}")


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()

    n = int(data[0])
    sequences = data[1:n + 1]

    solve(n, sequences)