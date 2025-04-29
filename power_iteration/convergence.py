"""Some code to test an idea to find the largest singular value of a matrix via power iteration, while always guaranteeing an overshoot."""

import numpy as np
from tqdm import tqdm


def analytical(A: np.ndarray) -> float:
    s = np.linalg.svd(A, compute_uv=False)
    return s[0]

def power_iteration(A: np.ndarray, eps: float, max_iters: int):
    _, n = A.shape
    v = np.random.randn(n)
    v /= np.linalg.norm(v)

    sigma_old = 0.0

    for _ in range(max_iters):
        Av = A @ v
        sigma_new = np.linalg.norm(Av)
        if sigma_new == 0:
            return 0.0

        v = A.T @ Av
        v /= np.linalg.norm(v)

        if abs(sigma_new - sigma_old) <= eps:
            break
        sigma_old = sigma_new

    return sigma_new + eps

def generate_and_test(num_matrices=10):
    results = []
    for _ in tqdm(range(num_matrices)):
        A = np.random.rand(np.random.randint(5, 15), np.random.randint(5, 15))
        sigma_power_iter = power_iteration(A, eps=0.0001, max_iters=100)
        sigma_exact = analytical(A)
        results.append((sigma_power_iter, sigma_exact))
    return results

if __name__ == "__main__": 
    trials = 1000000
    results = generate_and_test(trials)
    assert int(np.sum([a > b for a, b in results])) == trials, "Overshoot did not happen in all cases."
    print(f"Average difference between singular values: {np.mean([abs(a - b) for a, b in results])}")
