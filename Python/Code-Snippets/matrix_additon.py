def mat_add(mat1, mat2):
    m = len(mat1)
    n = len(mat1[0])
    c = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            c[i][j] = mat1[i][j] + mat2[i][j]
    return c


print(mat_add([
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6],
],
    [
    [4, 19, 12],
    [3, 35, 37],
    [8, 41, 26],
]))
