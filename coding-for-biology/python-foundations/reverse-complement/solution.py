dna = input().strip()

complement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

reverse_complement = ""

for base in reversed(dna):
    reverse_complement += complement[base]

print(reverse_complement)