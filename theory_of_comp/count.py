

from itertools import product

all_bin = [''.join(p) for p in product(["0", "1"], repeat=5)]
a = [s for s in all_bin if "01" in s and "11" not in s]
b = [s for s in all_bin if "11" in s and "01" not in s]
c = [s for s in all_bin if "11" in s and "00" not in s]

print(all_bin)
print(a, f"count: {len(a)}")
print(b, f"count: {len(b)}")
print(c, f"count: {len(c)}")