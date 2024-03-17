import random

def read_integer_in_range(prompt, a, b):
    while True:
        try: 
            n = int(input(prompt))
            if n < a: raise ValueError("number must >= %d" % a)
            elif n > b: raise ValueError("number must <= %d" % b)
            return n
        except ValueError as e:
            print("error: invalid number\n")

def game(a, b):
    x = random.randint(a, b)

    while True:
        n = read_integer_in_range(f"Enter guess ({a}-{b}): ", a, b)
        #print(x, n)

        if n == x:
            print("Correct!")
            break
        elif n < x - 10:
            print("Too low!")
        elif n > x + 10:
            print("Too high!")
        elif n < x - 5:
            print("Low!")
        elif n > x + 5:
            print("High!")
        elif abs(n - x) <= 5:
            print("Close!")

game(0, 100)