import numpy as np
from numpy.linalg import inv
from scipy.linalg import null_space

# defining the generators of the group D3

rho_r = np.array([
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0]
], dtype=int)

rho_s = np.array([
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0]
], dtype=int)

# computing the constraint for each of the generators


def compute_constraints(mat: np.array):
    inv_t = inv(mat).T
    kron = np.kron(mat, inv_t)
    minus_I = kron - np.eye(kron.shape[0])
    return minus_I


cons1 = compute_constraints(rho_r)
cons2 = compute_constraints(rho_s)

# stacked

M = np.vstack([cons1, cons2])
ns = null_space(M)

# extracting the functions

W_list = [vec.reshape((6, 6)) for vec in ns.T]

# testing equivariance

