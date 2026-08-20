import sys

s = sys.stdin.readline().strip()

upper = s.upper()
cleaned = ''.join(c for c in upper if c in 'ACGT')
removed = len(s) - len(cleaned)

print(cleaned)
print(removed)