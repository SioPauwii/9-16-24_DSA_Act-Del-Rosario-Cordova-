sent = input("Enter your sentence:\n")
str1 = input("\nEnter your string to replace: ")
str2 = input("Word replacement: ")

newSent  = sent.replace(str1, str2)

print(f'\nOld String: {sent}')
print(f'New String: {newSent}')