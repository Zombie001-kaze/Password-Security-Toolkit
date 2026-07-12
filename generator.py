import secrets
import string

def generate_password(length):
    characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()_+-=[]{}<>?"
    )

    return "".join(secrets.choice(characters) for _ in range(length))