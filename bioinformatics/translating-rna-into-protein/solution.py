import sys


def solve(rna: str) -> None:
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y",
        "UGU": "C", "UGC": "C", "UGG": "W",

        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",

        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

        "AUU": "I", "AUC": "I", "AUA": "I",
        "AUG": "M",

        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S",
        "AGA": "R", "AGG": "R",

        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    }

    stop_codons = {"UAA", "UAG", "UGA"}

    protein = []

    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]

        if codon in stop_codons:
            break

        protein.append(codon_table[codon])

    print("".join(protein))


if __name__ == "__main__":
    rna = sys.stdin.readline().strip()  # The RNA sequence to translate
    solve(rna)