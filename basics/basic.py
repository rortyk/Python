ranging = {
    'A': 100, 
    'B': 85,
    'C': 95
}

print(sorted(ranging, key=ranging.get, reverse=True))

s = "fklkjlgja;lgiaujogal"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)