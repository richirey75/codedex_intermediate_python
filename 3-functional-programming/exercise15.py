# In this lecture I recap what I learned in the previous lessons
# # Pure functions return output with no side effects.
# # Higher-order functions are used as arguments and/or return values.
# # map(), filter(), and reduce() can efficiently manipulate data.
# # List comprehensions can process existing list data in one line


import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

# Mapped names
def capitalize_suffix(name):
  return name.capitalize()

capped_suffixes = list(map(capitalize_suffix, suffixes))

def create_username(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

# List comprehensions
random_names = [
  create_username(prefixes, capped_suffixes) for name in range(10)  
]
print("Random Fantasy Names:", random_names)

# Filtered names
def fire_in_username(name):
  return 'Fire' in name
filtered_names = list(filter(fire_in_username, random_names))
print("Filtered Names with 'Fire':", filtered_names)

# Reduced list based on filtered names
def concatenate_names(acc, name):
  return acc + ', ' + name

reduced_names = reduce(concatenate_names, filtered_names)
print("Concatenated Names:", reduced_names)

def display_name_info():
  print("Fantasy Names:")
  for name in random_names:
    print(name)
  print()
  print('Filtered names with \'Fire\':', filtered_names)
  print('Concatenated names:', reduced_names) 

display_name_info()