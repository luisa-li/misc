import sympy as sp

# defining the generators of the group D3

rho_r = sp.Matrix([
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0]
])

rho_f = sp.Matrix([
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0]
])

# computing the constraint for each of the generators


def compute_constraints(mat):
    return sp.kronecker_product(mat, (mat.inv()).T) - sp.eye(36)


cons1 = compute_constraints(rho_r)
cons2 = compute_constraints(rho_f)

# stack constraints
M = sp.Matrix.vstack(cons1, cons2)

# compute nullspace
ns = M.nullspace()

# reshape
W_list = [v.reshape(6, 6) for v in ns]

# building the rest of the group representations
rho_e = sp.eye(6)
rho_r2 = rho_r * rho_r
rho_rf = rho_r * rho_f
rho_r2f = rho_r2 * rho_f

# checking commutativity 
for w in W_list:
    for g in [rho_e, rho_r, rho_r2, rho_f, rho_rf, rho_r2f]: 
        assert w * g == g * w
