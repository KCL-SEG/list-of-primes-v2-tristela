"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes>0:
        counter = 0
        i=2
        while counter<number_of_primes:
            if isPrime(i):
                list.append(i)
                counter = counter+1
            i = i+1
        return list
    else:
        raise ValueError


def isPrime(number):
    isPrime = True
    if isinstance(number, int):
        i = 2
        while i<(number/2)+1 and isPrime==True:
            if number%i==0:
                isPrime=False
            i = i+1
    else:
        isPrime = False
    return isPrime

#test
