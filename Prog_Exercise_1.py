str1 =  input('Enter your string: ')
pos = int(input('Enter the position to identify the character: '))

if (pos >= 0 and pos < len(str1)):
    charPos = str1[pos]
    print(f'The Character at position {pos} is {charPos}')
else:
    print(f'The position is out of bound')