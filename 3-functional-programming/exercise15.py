# In this lecture I recap what I learned in the previous lessons
# # Pure functions return output with no side effects.
# # Higher-order functions are used as arguments and/or return values.
# # map(), filter(), and reduce() can efficiently manipulate data.
# # List comprehensions can process existing list data in one line


import random

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(list_of_words):
    return [word.capitalize() for word in list_of_words]

# Don't overwrite the function name!
capitalized_suffixes = capitalize_suffix(suffixes)

print(capitalized_suffixes)
