def is_prime1(n):
    if n == 1: return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime2(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        
    return True

def read_natural_number(prompt):
    while True:
        try: 
            n = int(input(prompt))
            if n < 1: raise ValueError("number must be non-negative")
            return n
        except ValueError as e:
            print("error: invalid natural number\n")

n = read_natural_number("Enter natural number: ")

if is_prime1(n):
    print("%d is prime!" % n)
else:
    print("%d is not prime" % n)
