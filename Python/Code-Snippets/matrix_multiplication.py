def mat_multi(mat1, mat2):
    m = len(mat1)
    n = len(mat2)
    c = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(m):
                c[i][j] += mat1[i][k]*mat2[k][j]

    return c


print(mat_multi([
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6],
],
    [
    [4, 19, 12],
    [3, 35, 37],
    [8, 41, 26],
]))
