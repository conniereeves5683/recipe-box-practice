from werkzeug.security import generate_password_hash, check_password_hash

password = "secret123"  # demo password, not a real one!

hash_value = generate_password_hash(password)

print("Password:", password)
print("Hash:    ", hash_value)

print("Check correct:", check_password_hash(hash_value, "secret123"))
print("Check wrong:  ", check_password_hash(hash_value, "wrongpass"))