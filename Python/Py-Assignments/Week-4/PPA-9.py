matrix = [
    [
        int(x) for x in input().split(' ')
    ]
    for _ in range(int(input()))
]

s = int(input())

print(
    '\n'.join(
        ' '.join([str(s * x) for x in row])
        for row in matrix
    )
)
