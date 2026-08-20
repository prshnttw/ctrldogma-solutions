import sys

n = int(sys.stdin.readline())
valid_count = 0

for _ in range(n):
    line = sys.stdin.readline().rstrip('\n')
    fields = line.split(' ')
    
    # Rule 1: exactly two fields
    if len(fields) != 2:
        ident = fields[0] if fields and fields[0] != '' else '?'
        print(f"{ident} MALFORMED")
        continue
    
    ident, seq = fields
    
    # Rule 2: only A, C, G, T
    if any(c not in 'ACGT' for c in seq):
        print(f"{ident} BADCHARS")
        continue
    
    # Rule 3: length multiple of 3
    if len(seq) % 3 != 0:
        print(f"{ident} NOTCODON")
        continue
    
    # Valid
    print(f"{ident} OK")
    valid_count += 1

print(valid_count)