def linear_congruential_generator(a, seed, c, m, n):
    result = []
    X = seed
    for i in range(n):
        X = (a * X + c) % m
        result.append(X)
    return result

# Given parameters
a = 2175143
seed = 3553
c = 10653
m = 1000000

# Generate sequence
sequence = linear_congruential_generator(a, seed, c, m, 4)
print(sequence)