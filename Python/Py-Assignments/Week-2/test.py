# n = 101
# print(
#     [i**2 for i in range(1, n)]
# )

print(
    [i**2 for i in [int(x) for x in input().split(',')]]
)
