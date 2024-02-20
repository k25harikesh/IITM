phoneNumber = input()

isValidPhoneNumber = True

if int(phoneNumber[0]) not in [6, 7, 8, 9]:
    isValidPhoneNumber = False

if len(phoneNumber) != 10:
    isValidPhoneNumber = False

for i in range(1, 11):
    if phoneNumber.count(str(i)) > 7 or str(i) * 6 in phoneNumber:
        isValidPhoneNumber = False

print('valid' if isValidPhoneNumber else 'invalid')
