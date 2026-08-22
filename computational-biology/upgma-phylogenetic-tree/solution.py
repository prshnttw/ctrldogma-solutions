import sys


def solve(n: int, matrix: list[list[float]]) -> None:
    # Active cluster IDs
    active = set(range(n))

    # Size of each cluster
    size = {i: 1 for i in range(n)}

    # Distance between clusters
    distance = {
        i: {
            j: matrix[i][j]
            for j in range(n)
            if i != j
        }
        for i in range(n)
    }

    next_id = n

    for _ in range(n - 1):

        # Find closest pair.
        # Sorting by (distance, first_id, second_id)
        # automatically implements the tie-breaking rule.
        best_pair = None

        for i in active:
            for j in active:
                if i >= j:
                    continue

                pair = (distance[i][j], i, j)

                if best_pair is None or pair < best_pair:
                    best_pair = pair

        d, a, b = best_pair

        # Print merge
        print(f"{a} {b} {d:.4f}")

        # New cluster
        new_id = next_id
        next_id += 1

        size[new_id] = size[a] + size[b]
        distance[new_id] = {}

        # Calculate distance from new cluster to every
        # other active cluster.
        for c in active:
            if c == a or c == b:
                continue

            new_distance = (
                size[a] * distance[a][c]
                + size[b] * distance[b][c]
            ) / size[new_id]

            distance[new_id][c] = new_distance

        # Remove old clusters
        active.remove(a)
        active.remove(b)

        # Add new cluster
        active.add(new_id)

        # Make the distance matrix symmetric
        for c in active:
            if c != new_id:
                distance[c][new_id] = distance[new_id][c]


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()

    n = int(data[0])

    matrix = [
        list(map(float, data[i + 1].split()))
        for i in range(n)
    ]

    solve(n, matrix)