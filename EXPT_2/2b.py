def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to_limit(limit):
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    return primes

n = int(input("Enter n: "))
result = primes_up_to_limit(n)
print(f"Prime numbers up to {n} is {len(result)}. And those are \n {result}")
