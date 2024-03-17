def shorten(s):
    return ''.join(c
                   for c in s 
                   if c.lower() not in ('a', 'e', 'i', 'o', 'u'))

s = input("Enter string: ")
print(shorten(s))