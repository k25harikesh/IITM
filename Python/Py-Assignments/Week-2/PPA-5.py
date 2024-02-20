x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())

# slope is undefined when the denominator (x2 - x1) is equal to zero
if (x2 - x1) == 0:
    print('Vertical Line')

else:
    slope = (y2 - y1) / (x2 - x1)

    print(slope * (x3 - x1) + y1)  # y3

    if slope == 0:
        print('Horizontal Line')
    else:
        print('Positive Slope' if slope > 0 else 'Negative Slope')
