#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']
"""

person = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']

print(person)
die = input("chose a person on the list to replace: ")
add = input("enter the replacment: ")

person.insert(person.index(die), add)
person.remove(die)

print(person)