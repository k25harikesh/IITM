person1 = input().capitalize()
dob1 = input()

person2 = input().capitalize()
dob2 = input()

dob1_d = int(dob1[0:2])
dob1_m = int(dob1[3:5])
dob1_y = int(dob1[6:])

dob2_d = int(dob2[0:2])
dob2_m = int(dob2[3:5])
dob2_y = int(dob2[6:])

if dob1_y == dob2_y:
    if dob1_m == dob2_m:
        if dob1_d == dob2_d:
            print(person1 if person1 < person2 else person2)
        else:
            print(person1 if dob1_d > dob2_d else person2)
    else:
        print(person1 if dob1_m > dob2_m else person2)
else:
    print(person1 if dob1_y > dob2_y else person2)
