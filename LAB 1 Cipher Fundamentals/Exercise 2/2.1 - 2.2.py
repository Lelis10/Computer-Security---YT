def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1

# Part 1: Finding GCD
print("GCD of (7001, 10) is:", gcd(7001, 10))
print("GCD of (4539, 6) is:", gcd(4539, 6))

# Part 2: Checking if numbers are co-prime
a1, b1 = 5435, 634
a2, b2 = 5432, 634

print(f"Are {a1} and {b1} co-prime? : ", are_coprime(a1, b1))
print(f"Are {a2} and {b2} co-prime? : ", are_coprime(a2, b2))
