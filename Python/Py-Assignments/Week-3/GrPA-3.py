input()  # START

x = 0
y = 0
while True:
    move = input()

    if move == 'UP':
        y += 1
    elif move == 'DOWN':
        y -= 1

    elif move == 'RIGHT':
        x += 1
    elif move == 'LEFT':
        x -= 1

    else:  # STOP
        break

print(abs(x) + abs(y))
