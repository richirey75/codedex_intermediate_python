# In this lesson I learn about CVS files, and how I need to use the encoding parameter
# to read and write files in Python. I also learn about the csv module, which provides functionality

import csv

# Open the CSV file in 'read' mode
with open('Bestseller - Sheet1.csv', 'r', encoding="utf-8") as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)
  next(csv_reader)  # Skip the header row

  max_sales = 0
  for row in csv_reader:
    current_sales = float(row[4]) # Assuming the sales data is in the 5th column (index 4)
    # Check if the current sales are greater than the max sales
    if current_sales > max_sales:
      max_sales = current_sales
      bestselling_book = row
# Print the bestselling book
print(f'The bestselling book is: {bestselling_book[0]} by {bestselling_book[1]} with {max_sales} million sales.') 


with open('bestseller_info.csv', 'w', newline='') as file:
  # Create a CSV writer object
  csv_writer = csv.writer(file)
  csv_writer.writerow(['Books', 'Author', 'Sales in millions'])
  # Write the bestselling book information
  csv_writer.writerow([bestselling_book[0], bestselling_book[1], bestselling_book[4]])

print('Bestselling info written to bestseller_info.csv')

with open('bestseller_info.csv', 'r') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)
  # Read and print the contents of the file
  for row in csv_reader:
    print(row)
