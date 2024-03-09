def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, n):
    i = 0
    j = 0
    key = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key.append(S[(S[i] + S[j]) % 256])
    return bytes(key)

def rc4_encrypt(key, plaintext):
    S = ksa(key)
    keystream = prga(S, len(plaintext))
    ciphertext = bytes(bytearray(x ^ y for x, y in zip(plaintext, keystream)))
    return ciphertext

def rc4_decrypt(key, ciphertext):
    return rc4_encrypt(key, ciphertext)  # Decryption in RC4 is the same as encryption

def main():
    key = b'SecretKey'
    plaintext = b'Hello, world!'
    
    # Encryption
    encrypted_text = rc4_encrypt(key, plaintext)
    print("Encrypted:", encrypted_text.hex())
    
    # Decryption
    decrypted_text = rc4_decrypt(key, encrypted_text)
    print("Decrypted:", decrypted_text.decode('utf-8'))

if __name__ == "__main__":
    main()
