def modular_exponentiation(M, e, p):
    result = 1
    M = M % p
    while e > 0:
        if e % 2 == 1:
            result = (result * M) % p
        e = e // 2
        M = (M * M) % p
    return result

# Test cases
test_cases = [
    (101, 7, 293),  # i. message = 101, e=7, p = 293
    (4, 11, 79),    # ii. message = 4, e=11, p = 79
    (5, 5, 53)      # iii. message = 5, e=5, p = 53
]

for i, (message, e, p) in enumerate(test_cases, start=1):
    result = modular_exponentiation(message, e, p)
    print(f"({i}) Result for message={message}, e={e}, p={p}: {result}")
