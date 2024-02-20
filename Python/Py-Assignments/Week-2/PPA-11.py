rollNumber = int(input())

if rollNumber % 4 == 0:
    group = 'Emerald'

elif rollNumber % 4 == 1:
    group = 'Sapphire'

elif rollNumber % 4 == 2:
    group = 'Peridot'

elif rollNumber % 4 == 3:
    group = 'Ruby'

print(group)
