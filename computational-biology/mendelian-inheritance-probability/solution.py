import sys


def solve(k: int, m: int, n: int) -> None:
    total = k + m + n

    # Probability that the offspring is aa.
    p_aa = 0.0

    # Aa x Aa -> aa with probability 1/4
    p_aa += (m / total) * ((m - 1) / (total - 1)) * 0.25

    # Aa x aa -> aa with probability 1/2
    p_aa += (m / total) * (n / (total - 1)) * 0.5
    p_aa += (n / total) * (m / (total - 1)) * 0.5

    # aa x aa -> aa with probability 1
    p_aa += (n / total) * ((n - 1) / (total - 1))

    # Dominant phenotype = everything except aa
    p_dominant = 1 - p_aa

    print(f"{p_dominant:.5f}")


if __name__ == "__main__":
    k, m, n = map(int, sys.stdin.read().split())

    solve(k, m, n)