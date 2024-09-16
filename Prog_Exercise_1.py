str1 =  input('Enter your string: ')
pos = int(input('Enter the position to identify the character: '))

charPos = str1[pos]
if (pos >= 0 and pos < len(str1)):
    print(f'The Character at position {pos} is {charPos}')
else:
    print(f'The position is out of bound')
