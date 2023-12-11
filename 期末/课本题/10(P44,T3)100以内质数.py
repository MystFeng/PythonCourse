def is_prime(n):
    if n < 2:
        return None
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [num for num in range(1, 101) if is_prime(num)]
print(primes)