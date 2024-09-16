import itertools

def printPerms(string, lenOfString):

    perms  = itertools.product(string, repeat = lenOfString)

    for parts in perms:
        print(''.join(parts))

str1 = input('Enter the string to find all possible permutation: ')

print(f'The given string is: {str1}')
print(f'The permuted strings are: {printPerms(str1, len(str1))}')