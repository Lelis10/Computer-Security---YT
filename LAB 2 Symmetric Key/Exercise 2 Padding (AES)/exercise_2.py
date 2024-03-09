from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def aes_256_encrypt(data, key, padding_method):
    cipher = AES.new(key, AES.MODE_CBC)
    if padding_method == 'zero':
        padded_data = zero_pad(data.encode(), AES.block_size)
    else:
        padded_data = pad(data.encode(), AES.block_size, style=padding_method)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext, cipher.iv

def aes_256_decrypt(ciphertext, key, iv, padding_method):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    if padding_method == 'zero':
        unpadded_data = zero_unpad(decrypted_data)
    else:
        unpadded_data = unpad(decrypted_data, AES.block_size, style=padding_method)
    return unpadded_data.decode()

def zero_pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = b'\x00' * padding_length
    return data + padding

def zero_unpad(data):
    return data.rstrip(b'\x00')

# Sample data
data = "Computer Security"
key = b'ThisIsA256BitKey1234567890123456'
padding_methods = ['pkcs7', 'x923', 'iso7816', 'zero']

# Encryption and decryption tests
for method in padding_methods:
    encrypted_data, iv = aes_256_encrypt(data, key, method)
    decrypted_data = aes_256_decrypt(encrypted_data, key, iv, method)
    print(f"Padding method: {method.upper()}")
    print("Encrypted data:", binascii.hexlify(encrypted_data).decode())
    print("Decrypted data:", decrypted_data)
    print()
