L = input().split(',')

print(
    sorted(L, key=lambda word: len(word))[-1]
)
