string = input().lower()
output = ''

if 'a' in string:
    output += 'a'

if 'e' in string:
    output += 'e'

if 'i' in string:
    output += 'i'

if 'o' in string:
    output += 'o'

if 'u' in string:
    output += 'u'

print('none' if output == '' else output)
