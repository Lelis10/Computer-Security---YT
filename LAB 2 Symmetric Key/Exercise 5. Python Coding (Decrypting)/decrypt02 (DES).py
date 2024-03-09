from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import hashlib
import binascii

def pad(data, size=64):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

def unpad(data, size=64):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return unpadded_data

def encrypt(plaintext, key, mode):
    method = algorithms.TripleDES(key)
    cipher = Cipher(method, mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return ct

def decrypt(ciphertext, key, mode):
    method = algorithms.TripleDES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return pl

if __name__ == "__main__":
    ciphertext = input("Enter the cipher text (hexadecimal): ")
    key = input("Enter the encryption key: ")

    key_hash = hashlib.sha256(key.encode()).digest()[:8]  # Using the first 64 bits for DES key

    ciphertext_bytes = binascii.unhexlify(ciphertext)

    decrypted_plaintext = decrypt(ciphertext_bytes, key_hash, modes.ECB())

    plaintext_unpadded = unpad(decrypted_plaintext)

    print("Decrypted:", plaintext_unpadded.decode())
