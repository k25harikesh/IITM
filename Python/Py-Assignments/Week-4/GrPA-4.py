names = input().split(',')
dates = input().split(',')

members = [[] for _ in range(366)]

for i, name in enumerate(names):
    members[int(
        dates[i]
    )].append(name)

common = []
for names in members:
    for i, name_1 in enumerate(names):
        for name_2 in names[i + 1:]:
            common.append(
                [name_1, name_2] if name_1 < name_2 else [name_2, name_1]
            )
