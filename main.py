from collections import defaultdict


d = defaultdict(int)

h = "hejsvej"

for c in h:
    d[c] += 1

ab = "hejsvejx"

for c in ab:
    if c not in d:
        print("not in:", c)
    print(c,d[c])
