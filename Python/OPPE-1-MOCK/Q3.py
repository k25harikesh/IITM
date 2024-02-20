def matrix_type(M):
    m = len(M)
    flag = True
    d = []
    for i in range(m):
        for j in range(m):
            if i != j and M[i][j] != 0:
                flag = False
    if not flag:
        return 'non-diagonal'

    for i in range(m):
        d.append(M[i][i])

    # print(d)

    is_scalar = True
    is_identity = True
    for i in range(m):
        if d[i] != 1:
            is_identity = False
        if d[i] != d[0]:
            is_scalar = False

    if is_identity:
        return 'identity'

    if is_scalar:
        return 'scalar'

    return 'diagonal'


print(matrix_type(
    [
        [1, 0, 0], [0, 1, 0], [0, 0, 1]
    ]
))

print(matrix_type(
    [
        [2, 0, 0], [0, 2, 0], [0, 0, 2]
    ]
))

print(matrix_type(
    [
        [3, 0, 0], [0, 2, 0], [0, 0, 2]
    ]
))
