from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import binascii

def pad(data, size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

def unpad(data, size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return unpadded_data

def encrypt(plaintext, key, mode):
    method = algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return ct

def decrypt(ciphertext, key, mode):
    method = algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return pl

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    plaintext_bytes = plaintext.encode()

    # Use only first 24 bytes of the SHA256 hash for TripleDES key
    key_hash = hashlib.sha256(key.encode()).digest()[:24]

    print("Before padding:", plaintext)

    padded_plaintext = pad(plaintext_bytes)

    print("After padding (CMS):", binascii.hexlify(bytearray(padded_plaintext)))

    ciphertext = encrypt(padded_plaintext, key_hash, modes.ECB())

    print("Cipher (ECB):", binascii.hexlify(bytearray(ciphertext)))

    decrypted_plaintext = decrypt(ciphertext, key_hash, modes.ECB())

    plaintext_unpadded = unpad(decrypted_plaintext)

    print("Decrypted:", plaintext_unpadded.decode())