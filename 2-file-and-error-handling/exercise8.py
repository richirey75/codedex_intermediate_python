# In this lecture I learned about file operations in Python
# 
# .seek(): Moves the file pointer to a specified location
# .tell(): Returns the current position of the file pointer
# .read(): Reads the entire file
# .readline(): Reads a single line from the file
# .readlines(): Reads all lines in the file and returns them as a list
# .write(): Writes a string to the file
# .writelines(): Writes a list of strings to the file
# .flush(): Flushes the internal buffer, ensuring all data is written to the file
# .close(): Closes the file
# .truncate(): Truncates the file to a specified size


message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file: # is best to the with open, because it closes the file automatically

    file.write(message)


with open('sent_message.txt', 'r+') as file:
    content = file.read()
    file.seek(0)    

    unsent_message = 'This message has been unsent.'
    file.truncate(len(unsent_message))  
    file.write(unsent_message)

print('Original Message:', message)
print('Unsent Message:', unsent_message)


'''
# Task 1: The Secret Message
sent_message = "Hey there! This is a secret message."

# Save the sent message to a file
with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

# Task 2: Simulate Unsending the Message
with open('sent_message.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()

    # Move the cursor to the beginning of the file
    file.seek(0)

    # Modify the message to simulate unsending
    unsent_message = "This message has been unsent."

    # Truncate the file to the length of the modified message
    file.truncate(len(unsent_message))

    # Write the modified message to the file
    file.write(unsent_message)

# Display the modified message
print("Original Message:", original_message)
print("Unsent Message:", unsent_message)
'''