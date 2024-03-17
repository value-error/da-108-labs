s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

print()

if len(s1) > len(s2):
    print("The first string is longer")
elif len(s2) > len(s1):
    print("The second string is longer")
else:
    print("The strings are of equal length")