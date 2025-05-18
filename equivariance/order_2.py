import itertools
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np


def equality_pattern(index_tuple):
    """Return the equality pattern label of a tuple as integers."""
    label_map = {}
    next_label = 0
    pattern = []
    for val in index_tuple:
        if val not in label_map:
            label_map[val] = next_label
            next_label += 1
        pattern.append(label_map[val])
    return tuple(pattern)

def generate_patterns(n=5, ell=4):
    """Generate all index tuples and group them by equality pattern."""
    index_tuples = itertools.product(range(n), repeat=ell)
    pattern_dict = defaultdict(list)
    for t in index_tuples:
        pat = equality_pattern(t)
        pattern_dict[pat].append(t)
    return pattern_dict

def build_B_tensor(pattern_class, n=5, ell=4):
    """Create a tensor B_γ with 1s at entries matching the pattern class."""
    B = np.zeros((n,) * ell)
    for idx in pattern_class:
        B[idx] = 1
    return B

def flatten_tensor(tensor):
    """Flatten n x n x n x n to 25 x 25 assuming n = 5."""
    return tensor.reshape(25, 25)


n = 5
ell = 4
pattern_classes = generate_patterns(n=n, ell=ell)
sorted_patterns = sorted(pattern_classes.items(), key=lambda x: x[0])
B_stack = np.stack([build_B_tensor(indices, n=n, ell=ell) for _, indices in sorted_patterns])
B = B_stack.reshape(15, 25, 25)


fig, axs = plt.subplots(3, 5, figsize=(15, 9))
axs = axs.flatten()


for i in range(len(B_stack)):
    pattern = sorted_patterns[i][0]

    ax = axs[i]
    ax.imshow(B[i],  interpolation='none')
    ax.set_title(str(pattern))
    ax.axis('off')

plt.tight_layout()
plt.show()