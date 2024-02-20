xCoordinate = float(input())
yCoordinate = float(input())

if xCoordinate == 0:
    region = 'origin' if yCoordinate == 0 else 'y-axis'

elif yCoordinate == 0:
    region = 'x-axis'

elif yCoordinate > 0:
    region = 'first' if xCoordinate > 0 else 'second'
else:
    region = 'fourth' if xCoordinate > 0 else 'third'

print(region)
