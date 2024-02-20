x = float(input())

if x == int(x):
    print(int(x))  # floor
    print(int(x))  # ceil

elif x > 0:
    print(int(x))  # floor
    print(int(x) + 1)  # ceil

else:
    print(int(x) - 1)  # floor
    print(int(x))  # ceil
