import random
import string

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_user():
    return {
        "userName": f"testuser_{generate_random_string(6)}",
        "password": "Test@123!"
    }