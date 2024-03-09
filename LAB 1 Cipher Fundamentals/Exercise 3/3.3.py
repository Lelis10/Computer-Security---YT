def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(limit + 1) if primes[i]]

# Define the ranges
ranges = [(1000, 2000), (2000, 3000), (3000, 4000)]

# Find the highest prime number in each range
for i, (start, end) in enumerate(ranges, start=1):
    primes_in_range = sieve_of_eratosthenes(end)
    primes_in_range = [p for p in primes_in_range if p >= start]
    highest_prime = max(primes_in_range)
    print(f"Highest prime number in range {i}: {highest_prime}")