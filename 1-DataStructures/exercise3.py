# In this lecture I learn about dictionaries and how to use them
# Dictionaries are unordered collections that allow you to store and access data with 
# key:value pairs

# dictionaries important methods
# .keys() returns just the keys from a dictionary
# .values() returns just the values
# .items() returns a list of the key-value pairs as tuples

# Create a dictionary to store information about an artifact from the Met museum
artifact = {
  'artist': 'Arshile Gorky',
  'period': 'World War II',
  'date': '1944'
}

print(artifact)
print(artifact.keys())
print(artifact.values())
print(artifact.items())