from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import hashlib
import base64

def decrypt(ciphertext, key, mode):
    method = algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    try:
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data
    except Exception as e:
        print("Error:", str(e))
        return None

if __name__ == "__main__":
    cipher_b64 = input("Enter the cipher text: ")
    keys = ["hello", "ankle", "changeme", "123456"]

    ciphertext_bytes = base64.b64decode(cipher_b64)

    for key in keys:
        key_hash = hashlib.sha256(key.encode()).digest()  
        decrypted_plaintext = decrypt(ciphertext_bytes, key_hash, modes.ECB())
        if decrypted_plaintext:
            print("Decrypted with key {}: {}".format(key, decrypted_plaintext.decode()))
            break
