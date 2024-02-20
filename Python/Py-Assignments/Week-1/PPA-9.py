# '''

# A simple algorithm has to be designed to find out whether a student belongs to the Data Science branch or not. The input will be a student's roll number, which is of the form BR18B0000. Here, BR represents the branch code,
# 18
# 18 represents the year of joining, B represents the education level and
# 0000
# 0000 represents the specific identification given to the student of that batch. The branch code for Data Science is DS. Print True if the student belongs to Data Science branch and False otherwise.

# '''

# a = input()

# res = a[0:2]

# if res == "DS" :
#    print(True)
# else :
#     print(False)


print(True if input()[0:2] == 'DS' else False)
