# In this lecture we learn about list comprehensions
# # List comprehensions are a concise way to create lists in Python.
# # They allow you to generate a new list by applying an expression to each item in an existing iterable.


# # The syntax for a list comprehension is:
# # [expression for item in iterable if condition]

# Original approach using a loop
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
  squares.append(num ** 2)

# Using a list comprehension to square each number
squared_numbers = [num ** 2 for num in numbers]

# Displaying the outcomes
print('Original Numbers:', numbers)
print('Squared Numbers:', squared_numbers)

nums = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

even_numbers = [num for num in nums if num % 2 == 0]

print('Original Numbers: ', nums)
print('Even Numbers: ', even_numbers)