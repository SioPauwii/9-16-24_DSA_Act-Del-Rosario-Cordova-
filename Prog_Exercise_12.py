def addDigitsInStr(string):
    numList = [int(char) for char in string if not char.isalpha()]   
    num = 0

    for count in numList:
        num += count
    return num

str1= input('Given string is: ')
print(f'The sum of the digits in the string is: {addDigitsInStr(str1)}')