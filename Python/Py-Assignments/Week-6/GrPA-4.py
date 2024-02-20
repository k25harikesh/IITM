def is_magic(mat):
    n = len(mat)
    d1 = [mat[i][i] for i in range(n)]
    d2 = [mat[i][n - 1 - i] for i in range(n)]
    rowSum = [sum(row) for row in mat]
    colSum = [sum(row[col] for row in mat) for col in range(n)]
    diagonal_sum = [sum(d1), sum(d2)]
    return ('YES' if
            all(x == diagonal_sum[0]
                for x in [*diagonal_sum, *rowSum, *colSum])
            else 'NO')


# print(is_magic([
#     [4, 9, 2],
#     [3, 5, 7],
#     [8, 1, 6],
# ]))
