# In this lecture I learn about pure functions and impure functions
# Pure functions are functions that always produce the same output for the same input and have no side effects.
# Impure functions are functions that can produce different outputs for the same input and have side effects.

# Pure function example
def calculate_circle_area(radius):
    return 3.14 * radius * radius

radius = 5

area_of_a_circle = calculate_circle_area(radius)

print(f"The area of a circle with radius {radius} is: {area_of_a_circle}")
print(type(area_of_a_circle))