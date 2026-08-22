dna = input().strip()

counts = {"A": 0, "C": 0, "G": 0, "T": 0}

for nucleotide in dna:
    counts[nucleotide] += 1

print(counts["A"], counts["C"], counts["G"], counts["T"])