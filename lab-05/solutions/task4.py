def camel_case_to_snake_case(s):
    result = []

    last = ''
    for c in s:
        if c.isupper():
            result.append(c.lower())
        elif c.islower():
            if last.isupper():
                x = result.pop()
                if result: result.append("_")
                result.append(x)
            result.append(c)
        else:
            result.append(c)
        
        #print("".join(result))
        last = c

    return ''.join(result)

print(camel_case_to_snake_case("TheBestThing"))

print(camel_case_to_snake_case("URLDispatcher"))

print(camel_case_to_snake_case("openAPIResponse"))


"""

T he B est T hing

URLD ispatcher

open APIR esponse

"""