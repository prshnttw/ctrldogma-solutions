import sys


def solve(s: str, t: str) -> None:
    distance = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1

    print(distance)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    solve(s, t)