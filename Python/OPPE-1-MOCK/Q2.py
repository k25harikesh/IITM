seq = [int(x) for x in input().split(',')]
x = len(seq)//2
left_side = sum(seq[:x])
right_side = sum(seq[x:])

if left_side == right_side:
    print('balanced')
else:
    print('left-heavy' if left_side > right_side else 'right-heavy')
