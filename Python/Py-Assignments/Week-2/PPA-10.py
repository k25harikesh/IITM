x = float(input())

# print the greatest integer less than or equal to x
if x > 0 or x == int(x):
    print(int(x))
else:
    print(int(x) - 1)

# print the smallest integer greater than or equal to x
if x < 0 or x == int(x):
    print(int(x))
else:
    print(int(x) + 1)
