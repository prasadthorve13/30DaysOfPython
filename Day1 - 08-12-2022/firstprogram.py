print("Hello World!")

#List
list = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5] # order maintained, duplicates allowed, null not allowed
print(list)

#Dictionary
dictionary = {
    'first_name': 'ABC',
    'first_name': 'DEF',
    'last_name': 'XYZ',
    'age': 250,
    'is_married': True,
    'skills': [0, 1, 2, 3, 4, 5],
    'age': 250}       # order maintained, duplicates allowed but replaces old value, null not allowed
print(dictionary)

#Tuple
tuple = ("Mercury", "Venus", "Earth", "Mercury") #Planets
print(tuple) # order maintained, duplicates allowed, null not allowed

#Set
set = {3.14, 9.81, 2.7, 3.14} # order is not maintained, duplicates allowed but replaces old values, null not allowed
print(set)