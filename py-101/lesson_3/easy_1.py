# Q1
# numbers = [1, 2, 3]
# numbers[6] = 5
# This code will raise an IndexError because we are trying to access index 6, which is out-of-bounds for numbers.


# Q2: Prints True or False depending on whether the string ends with an exclamation mark
def ends_in_exclamation(string):
    return string[-1] == '!'

print(ends_in_exclamation("Come over here!")) # True
print(ends_in_exclamation("What's up, Doc?")) # False

# Q3
famous_words = "seven years ago..."
first_way = "Four score and " + famous_words
second_way = f"Four score and {famous_words}"

# Q4
munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description.capitalize())

# Q5
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())

# Q6
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
print('Dino' in str1)
print('Dino' in str2)

# Q7
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append('Dino')

# Q8
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(['Dino', 'Hoppy'])

# Q9
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
last_index = advice.find('house')
print(advice[:last_index])

# Q10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))