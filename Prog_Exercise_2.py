str1 = input('Enter your string to compare: ')
str2 = input('Enter the string to compate to: ')

if(str1 <  str2):
    print(f'"{str1}" is less than or comes before "{str2}"')
elif(str1 == str2):
    print(f'"{str1}" is equal to "{str2}"')
else:
    print(f'"{str1}" is more than or comes after "{str2}"')