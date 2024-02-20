# counting how many times a word came in a sequence.

s = ['hiii', 'hello', 'babu', 7868, 'r', 'sknd', 'sknd ', 'hiii']
p = set(s)
# print(len(s))
# print(len(p))
d = {}
# print(s)
for x in p:
    d[x] = 0
print(d)

for x in s:
    d[x] = d[x]+1

print(d)
