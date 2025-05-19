# In this lecture I learn about sets and how to use them in Python
# Sets are unordered collections of unique elements

# Three methods in particular
# .union(): Combines two or more sets and returns a new set
# .intersection(): Returns a set of items common to two or more sets
# .difference(): Returns a set of items found only in the calling set


# In this exercise, I will create two sets of fruits and perform union, intersection, and difference operations on them
set1 = {'apple', 'mango', 'strawberry', 'kiwi'}
set2 = {'kiwi', 'watermelon', 'orange'}

set_union = set1.union(set2)
set_intersection = set1.intersection(set2)
set_difference = set1.difference(set2)

print(set_union)
print(set_intersection)
print(set_difference)


# Here are some additional examples of set operations
my_fruits = {'apple', 'banana', 'kiwi'}
friend_fruits = {'banana', 'orange', 'grape'}

# Uncomment to check if a fruit is <in> both list
# print('apple' in fruits)  # Output: True
# set3 = {'apple', 'orange'}
# print(set3.issubset(fruits))  # Output: True

union_result = my_fruits | friend_fruits
intersection_result = my_fruits & friend_fruits
difference_result = my_fruits - friend_fruits

print('Union:', union_result)
print('Intersection:', intersection_result)
print('My Fruits - Friend\'s Fruits:', difference_result)