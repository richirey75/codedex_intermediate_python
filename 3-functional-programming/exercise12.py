# In this lecture I learn about higher-order functions
# Higher-order functions are functions that can take other functions as arguments or return them as results.
# They are a key concept in functional programming and allow for more abstract and flexible code.


# Define the Higher-order function 
def apply_operation(operation, numbers):
  result = []
  for num in numbers:
    result.append(operation(num))
  return result

# Example operation
def double(x):
  return x * 2

# List of numbers
numbers_list = [1, 2, 3, 4, 5]

# Using the higher-order function
doubled_numbers = apply_operation(double, numbers_list)

# Displaying the outcomes
print('Original Numbers:', numbers_list)
print('Doubled Numbers:', doubled_numbers)


def translator(language):
  translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
  }

  def translate(word):
    if word.lower() in translations[language]:
      return translations[language][word.lower()]
    else:
      return f'Word not found in {language}'
  
  return translate

translate_to_spanish = translator('french')
print(translate_to_spanish('hello'))  # Output: hola