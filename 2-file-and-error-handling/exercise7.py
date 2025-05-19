# In this lecture I learn about the file realm
# The three modes are:
# 'r' - read
# 'w' - write
# 'a' - append

file = open('example.txt', 'r')

content = file.read()

print('Using read():')
print(content)

line1 = file.readline()  # Read the first line
print(line1, end='')     # Printing the first line

line2 = file.readline()  # Read the second line
print(line2, end='')     # Printing the second line

file.close()