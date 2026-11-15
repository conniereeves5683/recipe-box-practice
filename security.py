from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(plain_password: str) -> str:
    """Return a safe hash to store in the password_hash column."""
    return generate_password_hash(plain_password)


def verify_password(stored_hash: str, candidate_password: str) -> bool:
    """Return True if the candidate matches the stored hash."""
    return check_password_hash(stored_hash, candidate_password)


