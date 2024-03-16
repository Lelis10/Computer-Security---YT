import random

# Function to calculate modular exponentiation
def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Function to generate keys
def generate_keys(p, g):
    private_key = random.randint(2, p - 1)
    public_key = mod_exp(g, private_key, p)
    return private_key, public_key

# Function for encryption
def encrypt(p, g, y, m):
    k = random.randint(2, p - 1)
    c1 = mod_exp(g, k, p)
    c2 = (m * mod_exp(y, k, p)) % p
    return c1, c2

# Function for decryption
def decrypt(p, x, c1, c2):
    s = mod_exp(c1, x, p)
    decrypted_message = (c2 * mod_exp(s, p - 2, p)) % p
    return decrypted_message

# Public parameters
p = 23
g = 5
y = 19
m = 10

# Generate keys
x, _ = generate_keys(p, g)

# Encrypt message
c1, c2 = encrypt(p, g, y, m)

print("Encrypted message:", (c1, c2))

# Decrypt message
decrypted_message = decrypt(p, x, c1, c2)

print("Decrypted message:", decrypted_message)
