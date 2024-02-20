n = int(input())

sequence = [
    [int(x) for x in input().split(',')]
    for _ in range(n)
]
px, py = [int(x) for x in input().split(',')]


def distance(point):
    return (
        (point[0] - px) ** 2 + (point[1] - py) ** 2
    ) ** .5


nearest = []

min_distance = distance(sequence[0])
for point in sequence:
    point_distance = distance(point)

    if point_distance < min_distance:
        min_distance = point_distance
        nearest = [','.join([str(x) for x in point])]

    elif point_distance == min_distance:
        nearest.append(','.join([str(x) for x in point]))

print('\n'.join(
    nearest
))
