'''
http://fusharblog.com/solving-linear-recurrence-for-programming-contest/
'''


def modular_mult(a, b, m):
    return ((a % m) * (b % m)) % m


def modular_sum(a, b, m):
    return ((a % m) + (b % m)) % m


def modular_multiply_matrix(m, n, mod):
    lim_c = len(m[0])
    lim_l = len(n)

    mn = [[0] * lim_c for x in range(0, lim_l)]

    for i in range(0, lim_l):
        for j in range(0, lim_c):
            for k in range(0, lim_l):
                acc = modular_mult(m[j][k], n[i][k], mod)
                mn[i][j] = modular_sum(mn[i][j], acc, mod)
    return mn


def exponential_by_squaring(mat, e, mod):
    copy_mat = mat
    while e > 1:
        if (e & 1) == 0:
            copy_mat = modular_multiply_matrix(copy_mat, copy_mat, mod)
            e >>= 1
        else:
            copy_mat = modular_multiply_matrix(mat, copy_mat, mod)
            e -= 1
    return copy_mat


print(int(10E9) + 7)

matrices = [
        [[1, 1], [1, 0]]
    ,[[0, 1], [1, 1]]
]

print(exponential_by_squaring(matrices[0], 10, int(10E9) + 7))
print(exponential_by_squaring(matrices[1], 10, int(10E9) + 7))

if __name__ == '__main__':
    pass
