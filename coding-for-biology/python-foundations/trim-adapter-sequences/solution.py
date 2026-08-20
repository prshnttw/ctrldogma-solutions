import sys


def main():
    # Read all input lines from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    adapter = input_data[0].strip()
    n = int(input_data[1].strip())
    reads = input_data[2 : 2 + n]

    trimmed_count = 0

    for read in reads:
        read = read.strip()
        # Find the index of the first occurrence of the adapter
        idx = read.find(adapter)

        if idx != -1:
            # If found, print everything before the adapter and increment count
            print(read[:idx])
            trimmed_count += 1
        else:
            # If not found, print the read unchanged
            print(read)

    # Print total count of trimmed reads on the final line
    print(trimmed_count)


if __name__ == "__main__":
    main()