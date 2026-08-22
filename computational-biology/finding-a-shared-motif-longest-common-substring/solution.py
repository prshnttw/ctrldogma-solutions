import sys


def solve(n: int, sequences: list) -> None:
    # Use the shortest sequence as the reference.
    reference = min(sequences, key=len)

    # best_lengths[i] = longest common substring ending at reference[i]
    best_lengths = [len(reference)] * len(reference)

    for sequence in sequences:
        current = [0] * len(reference)
        previous = [0] * len(reference)

        for j, char in enumerate(sequence):
            for i, ref_char in enumerate(reference):
                if ref_char == char:
                    current[i] = previous[i - 1] + 1 if i > 0 else 1
                else:
                    current[i] = 0

        # The above DP alone is for one sequence.
        # We need the best common suffix length for every position
        # in the reference sequence.
        #
        # Recalculate while retaining the maximum suffix length
        # ending at each reference position.
        previous = [0] * (len(reference) + 1)
        max_for_sequence = [0] * len(reference)

        for j in range(1, len(sequence) + 1):
            current = [0] * (len(reference) + 1)

            for i in range(1, len(reference) + 1):
                if reference[i - 1] == sequence[j - 1]:
                    current[i] = previous[i - 1] + 1
                    max_for_sequence[i - 1] = max(
                        max_for_sequence[i - 1],
                        current[i]
                    )

            previous = current

        # Restrict the common length to what this sequence supports.
        best_lengths = [
            min(best_lengths[i], max_for_sequence[i])
            for i in range(len(reference))
        ]

    best = ""

    for i, length in enumerate(best_lengths):
        if length > 0:
            candidate = reference[i - length + 1:i + 1]

            if (
                length > len(best)
                or (length == len(best) and candidate < best)
            ):
                best = candidate

    print(best)


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()

    n = int(data[0].strip())
    sequences = [line.strip() for line in data[1:1 + n]]

    solve(n, sequences)