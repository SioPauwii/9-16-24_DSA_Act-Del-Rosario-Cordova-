str1 = input('Enter your string to compare: ')
str2 = input('Enter the string to compate to: ')

if(str1.lower() == str2.lower()):
    print(f'"{str1}" is equal to "{str2}"')
else:
    print(f'"{str1}" is not equal to "{str2}"')