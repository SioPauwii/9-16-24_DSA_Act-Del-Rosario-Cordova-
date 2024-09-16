def dupCheck(string):

    chars = []

    print('The duplicate characters and counts are:')

    for char in string:
        if string.count(char) > 1 and char not in chars:   
            print(f'{char} appears {string.count(char)} times')
            chars.append(char)


str1 = input('The given string is: ')

dupCheck(str1)