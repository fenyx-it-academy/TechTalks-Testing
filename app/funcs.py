def inc(x):
    """ increments a given int with 1 and returns the value """
    return x + 1

def subt(x):
    """ subtracts 1 from a given int and returns the value """
    return x - 1


def reverse_word(word):
    """ reverses a given word and returns the value """
    return word[::-1]


def prime_number(number):
    """ checks if a given number is prime or not"""

    for i in range(2, number):
        if number % i == 0:
            return f'{number} is not a prime number'
    return f'{number} is a prime number'


















    # if number < 2:
    #     return f'{number} is not a prime number'