List = [11,53,65,76,89,211]
num = int(input('Enter a number: '))
print (all(x>=num for x in List))
