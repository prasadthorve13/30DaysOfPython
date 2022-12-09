#List
list = [0, 1, 2, 3, 4, 5, 0, 'a', True, 1, 2, 3, 4, 5]
print(list) # heterogeneous, order maintained, duplicates allowed, null not allowed

#Dictionary
dictionary = {
    'first_name': 'ABC',
    'first_name': 'DEF',
    'last_name': 'XYZ',
    'age': 250,
    'is_married': True,
    'skills': [0, 1, 2, 3, 4, 5],
    'age': 250}       # heterogeneous, order maintained, duplicates allowed but replaces old value, null not allowed
print(dictionary)

#Tuple
tuple = ("Mercury", "Venus", "Earth", "Mercury", 1, True) # Planets
print(tuple) # heterogeneous, order maintained, duplicates allowed, null not allowed

#Set
set = {3.14, 9.81, 2.7, 3.14, True, 'a'}
print(set)  # heterogeneous, order is not maintained, duplicates allowed but replaces old values, null not allowed