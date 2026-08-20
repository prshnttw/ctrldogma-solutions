import sys


def main():
    # Read all input lines from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0].strip())
    seqs = [line.strip() for line in input_data[1 : 1 + n] if line.strip()]

    # 1. Count: number of sequences
    count = len(seqs)

    # Precompute lengths using a list comprehension
    lengths = [len(seq) for seq in seqs]

    # 2. Total: total bases across all sequences
    total_bases = sum(lengths)

    # 3. Mean: mean sequence length to two decimal places
    mean_length = total_bases / count

    # 4. Longest: length of the longest sequence
    longest_length = max(lengths)

    # 5. GC-rich: count sequences with GC content strictly above 50%
    # GC content = (count of G + count of C) / total length
    gc_rich_count = sum(
        1 for seq in seqs if (seq.count("G") + seq.count("C")) / len(seq) > 0.5
    )

    # Output the five formatted statistics
    print(f"Count: {count}")
    print(f"Total: {total_bases}")
    print(f"Mean: {mean_length:.2f}")
    print(f"Longest: {longest_length}")
    print(f"GC-rich: {gc_rich_count}")


if __name__ == "__main__":
    main()