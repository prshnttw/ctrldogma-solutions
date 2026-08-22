s = input().strip()

complement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

reverse_complement = ''.join(complement[base] for base in reversed(s))

if s == reverse_complement:
    print("YES")
else:
    print("NO")