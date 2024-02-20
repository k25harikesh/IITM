def transpose(mat):

    clm = [[row[col] for row in mat] for col in range(len(mat[0]))]
    return clm


print(transpose([
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6],
]))
