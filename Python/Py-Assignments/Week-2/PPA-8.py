start = input()
end = input()

xDistance = abs(
    ord(start[0]) - ord(end[0])
)
yDistance = abs(
    int(start[1]) - int(end[1])
)

print('YES' if xDistance == yDistance else 'NO')
