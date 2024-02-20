n = int(input())

if (n <= 5):
    print("NO SOLUTION")

else:
    for x in range(1, n):
        for y in range(x, n):
            z = (x ** 2 + y ** 2) ** 0.5
            if (z == int(z)) and z < n:
                print(x, y, int(z), sep=',')
