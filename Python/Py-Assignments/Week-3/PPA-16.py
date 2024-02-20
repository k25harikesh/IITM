marks = int(input())
nosOptions = int(input())
seqCorrectOptions = [int(x) for x in input().split(',')]
seqChosenOptions = [int(x) for x in input().split(',')]

wrong = False
for option in seqChosenOptions:
    if option not in seqCorrectOptions:
        wrong = True
        break

print(0.0 if wrong else len(seqChosenOptions) * marks / len(seqCorrectOptions))
