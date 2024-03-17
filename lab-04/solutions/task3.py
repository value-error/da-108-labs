import string

def get_username():
    chars = string.ascii_letters + string.digits + "_"

    while True:
        try:
            s = input("Enter username: ")
            s = s.strip()

            if len(s) < 5:
                raise ValueError("username must be at least 5 characters")
            
            if s[0] not in string.ascii_letters:
                raise ValueError("username must start with a letter")

            for c in s:
                if c not in chars:
                    raise ValueError("username must only contain letters, digits and underscore")
            
            return s
        except ValueError as e:
            print("error:", e)
            print()

username = get_username()

print()

print('"%s" is a valid username!' % username)