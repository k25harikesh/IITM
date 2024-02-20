word = input()

if 'a' and 'e' and 'i' and 'o' and 'u' in word and \
        word.index('a') < word.index('e') and word.index('e') < word.index('i') and \
        word.index('i') < word.index('o') and word.index('o') < word.index('u') and \
        word.count('a') >= word.count('e') and word.count('e') >= word.count('i') and \
        word.count('i') >= word.count('o') and word.count('o') >= word.count('u'):
    print('It is a perfect word')

else:
    print('It is not a perfect word')
