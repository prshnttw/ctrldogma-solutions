dna = input().strip()

gc_count = dna.count('G') + dna.count('C')
gc_content = (gc_count / len(dna)) * 100

print(f"{gc_content:.2f}")