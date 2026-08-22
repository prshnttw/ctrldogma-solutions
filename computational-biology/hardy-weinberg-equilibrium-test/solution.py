import sys


def solve(n_AA: int, n_Aa: int, n_aa: int) -> None:
    # Total number of individuals
    N = n_AA + n_Aa + n_aa

    # Allele frequencies
    p = (2 * n_AA + n_Aa) / (2 * N)
    q = 1 - p

    # Expected genotype counts
    expected_AA = p * p * N
    expected_Aa = 2 * p * q * N
    expected_aa = q * q * N

    observed = [n_AA, n_Aa, n_aa]
    expected = [expected_AA, expected_Aa, expected_aa]

    # Chi-square statistic
    chi_square = 0.0

    for obs, exp in zip(observed, expected):
        if exp != 0:
            chi_square += (obs - exp) ** 2 / exp

    print(f"{p:.4f}")
    print(f"{chi_square:.4f}")


if __name__ == "__main__":
    data = sys.stdin.read().split()

    n_AA = int(data[0])
    n_Aa = int(data[1])
    n_aa = int(data[2])

    solve(n_AA, n_Aa, n_aa)