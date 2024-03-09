from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from binascii import hexlify

def chacha20_encrypt(key, nonce, plaintext):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def chacha20_decrypt(key, nonce, ciphertext):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    key = b'qwerty' + (32 - len(b'qwerty')) * b'\x00'  # Padding the key to 32 bytes
    nonce = bytes.fromhex('0000000000000000')

    # Ciphertexts provided
    ciphertexts = [
        bytes.fromhex('e81461e995'),
        bytes.fromhex('eb057fe49e34'),
        bytes.fromhex('e8127ee691315e'),
        bytes.fromhex('fb0562f592304385d4')
    ]

    # Decrypt ciphertexts
    for ciphertext in ciphertexts:
        plaintext = chacha20_decrypt(key, nonce, ciphertext)
        print(plaintext.decode('utf-8'))

if __name__ == "__main__":
    main()
