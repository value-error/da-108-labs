def factorial(n):
    f = 1

    for i in range(2, n + 1):
        f *= i

    return f

def read_whole_number(prompt):
    while True:
        try: 
            n = int(input(prompt))
            if n < 0: raise ValueError("number must be non-negative")
            return n
        except ValueError as e:
            print("error: invalid whole number\n")

n = read_whole_number("Enter a non-negative number: ")
print("%d! = %d" % (n, factorial(n)))