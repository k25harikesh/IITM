n = int(input())

matrix_1 = [
    [int(x) for x in input().split(',')]
    for _ in range(n)
]

matrix_2 = [
    [int(x) for x in input().split(',')]
    for _ in range(n)
]

print(
    '\n'.join(
        ','.join([
            str(matrix_1[j][i] + matrix_2[j][i]) for i in range(n)
        ])
        for j in range(n)
    )
)
