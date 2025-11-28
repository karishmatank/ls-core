# Write a function build_profile that takes a first name and a last name, 
# and any number of keyword arguments to add to a user's profile.

# Example:
# print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# # {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}

def build_profile(first_name, last_name, **kwargs):
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(kwargs)
    return profile

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}
