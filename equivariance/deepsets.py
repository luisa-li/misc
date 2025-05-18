import numpy as np


def build_equivariant_matrix(M, lambda_val, gamma_val):
    I = np.eye(M)
    one_one_T = np.ones((M, M))
    return lambda_val * I + gamma_val * one_one_T

def build_symmetric_matrix(M):
    A = np.random.randn(M, M)
    return (A + A.T) / 2

def build_permutation_matrix(M):
    perm = np.random.permutation(M)
    P = np.zeros((M, M))
    P[np.arange(M), perm] = 1
    return P

def sanity_check_1():

    x = np.array([[1, 3, 5],
                    [2, 4, 6]])

    lmbda = np.array([[7, 8, 9],
                    [10, 11, 12],
                    [23, 24, 25]])

    x2 = np.array([[2, 4, 6],
                    [1, 3, 5]])

    oneone = np.array([[1, 1], [1, 1]])

    tau = np.array([[13, 14, 15],
                    [16, 17, 18],
                    [19, 21, 22]])

    o1 = x @ lmbda - oneone @ x @ tau
    o2 = x2 @ lmbda - oneone @ x2 @ tau

def sanity_check_2():
    
    weight = build_equivariant_matrix(10, 2, 3)
    symmetric = build_symmetric_matrix(10)
    permutation = build_permutation_matrix(10)
    
    lhs = permutation @ weight @ symmetric
    rhs = weight @ permutation @ symmetric
    
    assert ((lhs - rhs) < 0.001).all()
    breakpoint()
        
sanity_check_2()