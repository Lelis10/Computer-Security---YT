import hashlib
text = "Computer Security"

# MD5
md5_hash = hashlib.md5(text.encode()).hexdigest()
print("MD5:", md5_hash)

# SHA-1
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
print("SHA-1:", sha1_hash)

# SHA-256
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print("SHA-256:", sha256_hash)

# SHA-384
sha384_hash = hashlib.sha384(text.encode()).hexdigest()
print("SHA-384:", sha384_hash)

# SHA-512
sha512_hash = hashlib.sha512(text.encode()).hexdigest()
print("SHA-512:", sha512_hash)