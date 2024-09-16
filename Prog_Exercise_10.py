def maskString(str1, maskstr):

    setOfCh = set(maskstr)

    processedStr =  ''

    for letter in str1:
        if letter not in setOfCh:
            processedStr += letter

    return processedStr

string = input('Enter the given string: ')
mask = input('Enter the mask string: ')

stringReborn = maskString(string, mask)

print(f'The new string is:  {stringReborn}')