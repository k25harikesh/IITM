'''

You are given a string and two non-negative integers as input. The two integers specify the start and end indices of a substring in the given string. Create a new string by replicating the substring a minimum number of times so that the resulting string is longer than the input string.

The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive) each on a different line.

'''

str  = input()
strt = int(input())
end  = int(input())

substr = str[strt:end+1]
nwstr = ""

while (len(nwstr)<=len(str)):    
    nwstr = nwstr+substr

print(nwstr)