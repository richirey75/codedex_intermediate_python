# In this lecture I learn about tuples and how they are different from lists
# tuples are immutable, meaning they cannot be changed after they are created
# you can access the elements of a tuple using indexing, just like a list


# In this exercise I will create a 3 tuples of my friends locations and print them out
# and also create a tuple of all my friends locations

san_dimas = (34.1067, 117.8067)
rancho_cucamonga = (34.1064, 117.5931)
glendora = (34.1361, 117.8653)

friends_location = san_dimas + rancho_cucamonga + glendora

print(san_dimas, rancho_cucamonga, glendora) 
print(friends_location)