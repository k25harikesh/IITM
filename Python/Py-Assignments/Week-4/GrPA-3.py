n = int(input())

matrix_1 = [
    [int(x) for x in input().split(',')]
    for _ in range(n)
]

matrix_2 = [
    [int(x) for x in input().split(',')]
    for _ in range(n)
]

product = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(str(
            sum(
                [matrix_1[i][k] * matrix_2[k][j] for k in range(n)]
            )
        ))
    product.append(','.join(row))

print('\n'.join(product))
