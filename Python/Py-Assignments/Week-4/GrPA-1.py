sequence = input().split(' ')
word = input()

print('YES' if word in sequence else 'NO')
if word in sequence:
    print(sequence.count(word))
