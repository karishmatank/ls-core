# Create a function create_user that takes a username and requires keyword-only arguments for email and age.

# Examples
# print(create_user("Srdjan", email="srdjan@example.com", age=39))
# # {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
# print(create_user("Srdjan", "srdjan@example.com", age=39))
# # Raises an exception

def create_user(username, *, email, age):
    return {
        'username': username,
        'email': email,
        'age': age
    }

print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
print(create_user("Srdjan", "srdjan@example.com", age=39))
# Raises an exception