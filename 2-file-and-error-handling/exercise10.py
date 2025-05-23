# In this lesson I recap what I learned in the previous lessons
# file handling, using the 
# .read()
# .write()
# .readline()
# .readlines()
# .writelines()
# .seek()
# .trouncate()
# CVS files how to read and write them and csv module

import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
    with open('packing_list.csv', 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print('Packing list file not found. Creating a new one.')
    with open('packing_list.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)

        csv_writer.writerows(data)

           
