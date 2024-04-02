'''
 Write a function that returns a list of prime numbers up to a given number using lambda.

'''

def generate_primes(n):
    is_prime = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1
    primes = list(filter(is_prime, range(2, n + 1)))
    return primes



n = 20
print("Prime numbers up to", n, ":", generate_primes(n))
