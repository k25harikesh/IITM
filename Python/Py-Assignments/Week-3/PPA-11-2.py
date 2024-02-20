n = int(input())

# the first pythagorean triple is 3, 4, and 5
if n <= 5:
    print('NO SOLUTION')

else:
    triplets = []
    for z in range(5, n):
        for y in range(4, z):
            for x in range(3, y):
                if x ** 2 + y ** 2 == z ** 2:
                    triplets.append([x, y, z])

    while triplets:
        min = triplets[0]
        for j in triplets:
            if j[0] < min[0] or \
                (j[0] == min[0] and j[1] < min[1]) or \
                    (j[0] == min[0] and j[1] == min[1] and j[2] < min[2]):
                min = j
        triplets.remove(min)
        print(f'{min[0]},{min[1]},{min[2]}')
