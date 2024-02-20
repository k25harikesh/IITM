n = int(input())

print(
    '\n'.join(
        ','.join(
            ['1' if i == j else '0' for i in range(n)]
        ) for j in range(n)
    )
)
