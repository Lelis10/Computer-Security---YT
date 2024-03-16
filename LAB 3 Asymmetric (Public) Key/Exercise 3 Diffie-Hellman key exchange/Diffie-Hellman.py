def calculate_public_key(private_key, base, prime):
    return (base ** private_key) % prime

def calculate_shared_secret(public_key, private_key, prime):
    return (public_key ** private_key) % prime

# Given parameters
prime = 23
base = 5

# Alice's private key
alice_private_key = 6
# Bob's private key
bob_private_key = 15

# Calculate public keys for Alice and Bob
alice_public_key = calculate_public_key(alice_private_key, base, prime)
bob_public_key = calculate_public_key(bob_private_key, base, prime)

# Calculate shared secret keys for Alice and Bob
alice_shared_secret = calculate_shared_secret(bob_public_key, alice_private_key, prime)
bob_shared_secret = calculate_shared_secret(alice_public_key, bob_private_key, prime)

# Verify if shared secret keys match
if alice_shared_secret == bob_shared_secret:
    print("Shared secret keys match!")
    print("Shared Secret Key:", alice_shared_secret)
else:
    print("Error: Shared secret keys do not match!")

