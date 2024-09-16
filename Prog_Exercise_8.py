def longestPalin(string):
    def palindromeCheck(left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]
    
    longPal = ""
    
    for i in range(len(string)):
        # Check for odd-length palindromes
        pal1 = palindromeCheck(i, i)
        # Check for even-length palindromes
        pal2 = palindromeCheck(i, i + 1)

        # Update the longest palindrome found
        if len(pal1) > len(longPal):
            longPal = pal1
        if len(pal2) > len(longPal):
            longPal = pal2

    return longPal

# Input from user
wholeStr = input('Enter your sequence of strings(sentence):\n')

# Normalize the string
wholeStr = wholeStr.lower().replace(' ', '')

# Find the longest palindromic substring
maxedOutPalindrome = longestPalin(wholeStr)

# Print the results
print(f'The given string is {wholeStr}')
print(f'The longest palindrome substring in the given string is: {maxedOutPalindrome}')
print(f'The length of the palindrome is {len(maxedOutPalindrome)}')
