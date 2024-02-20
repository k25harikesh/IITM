string = input()

try:
    float(string)
    print('Float' if '.' in string else 'Integer')
except:
    print('None')
