# import sys


# def solve(identifier: str, seq: str) -> None:
#     print(f"ID: {identifier}")
#     print(f"Length: {len(seq)}")
#     print(f"First base: {seq[0]}")


# if __name__ == "__main__":
#     identifier = sys.stdin.readline().strip()
#     seq = sys.stdin.readline().strip()
#     solve(identifier, seq)

import sys


def solve(s: str, t: str) -> None:
    positions = []

    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(str(i + 1))  # 1-based indexing

    print(" ".join(positions))


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    solve(s, t)