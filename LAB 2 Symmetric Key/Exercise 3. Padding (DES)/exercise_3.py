from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import binascii

def des_encrypt(data, key, padding_method):
    cipher = DES.new(key, DES.MODE_ECB)
    if padding_method == 'zero':
        padded_data = zero_pad(data.encode(), DES.block_size)
    else:
        padded_data = pad(data.encode(), DES.block_size, style=padding_method)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

def des_decrypt(ciphertext, key, padding_method):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    if padding_method == 'zero':
        unpadded_data = zero_unpad(decrypted_data)
    else:
        unpadded_data = unpad(decrypted_data, DES.block_size, style=padding_method)
    return unpadded_data.decode()

def zero_pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = b'\x00' * padding_length
    return data + padding

def zero_unpad(data):
    return data.rstrip(b'\x00')

# Sample data
data = "Hello, DES!"
key = b'Eightkey'

# Padding methods for DES
padding_methods = ['pkcs7', 'x923', 'iso7816', 'zero']

# Encryption and decryption tests
for method in padding_methods:
    encrypted_data = des_encrypt(data, key, method)
    decrypted_data = des_decrypt(encrypted_data, key, method)
    print(f"Padding method: {method.upper()}")
    print("Encrypted data:", binascii.hexlify(encrypted_data).decode())
    print("Decrypted data:", decrypted_data)
    print()
