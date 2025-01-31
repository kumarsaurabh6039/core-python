# List Comprehension
# Squares of Odd Numbers:
# Create a list of squares for all odd numbers between 1 and 20.
# list1 =[i**2 for i in range (1,20) if i% 2 != 0]
# print(list1)

# Extract Uppercase Letters:
# Given a string, extract all uppercase letters into a list using a comprehension.
# Example: Input "Hello World" → Output ['H', 'W']
# str = 'Hello World'
# uppercase_letters = [char for char in str if char.isupper()]
# print(uppercase_letters)

# Reverse Strings:
# Create a new list with each string reversed from a given list of strings.
# Example: Input ['hello', 'world'] → Output ['olleh', 'dlrow']
# list = ['hello','world']
# rev_of_list = [i[::-1] for i in list]
# print(rev_of_list)

#######################################################################
#####################################################################333

# Divisible by 3 and 5:
# Find all numbers between 1 and 100 that are divisible by both 3 and 5.
# list1 = [i for i in range(1,100) if i%3==0 and i%5==0]
# print(list1)
##################################################################################
#############################################################################

# Dictionary Comprehension:-

# Word Length Dictionary:
# Given a list of words, create a dictionary where the keys are the words, and the values are their lengths.
# Example: Input ['apple', 'banana', 'cherry'] → Output {'apple': 5, 'banana': 6, 'cherry': 6}
# dict1 = ['apple','banana','cherry']
# word_lengths = {word: len(word) for word in dict1}
# print(word_lengths)
###############################################################################
##################################################################
# Number Classification:
# Create a dictionary where numbers from 1 to 20 are keys, and their values are "Prime" or "Composite" based on their nature.

# Square Roots Dictionary:
# Create a dictionary where the keys are numbers from 1 to 10, and the values are their square roots.
# square_roots = {i**2 for x in range(1, 11)}
# print(square_roots)

################################################################################
####################################################################################

# Set Comprehension
# Unique Vowels:
# Extract all unique vowels from a given string.
# Example: Input "comprehensions" → Output {'o', 'e', 'i'}
# string = "comprehensions"
# unique_vowels = {char for char in string if char in 'aeiou'}
# print(unique_vowels)

# Square Numbers Set:

# Generate a set of squares for all numbers from 1 to 10.
# set = {i**2 for i in range(1,10)}
# print(set)

#####################################################
####################################################3

# Nested Comprehension
# Transpose a Matrix:
# Given a 2D list, write a comprehension to transpose the matrix.
# Example: Input [[1, 2, 3], [4, 5, 6]] → Output [[1, 4], [2, 5], [3, 6]]
# matrix = [[1, 2, 3], [4, 5, 6]]
# transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transpose)

# Pair Combinations:
# Generate all possible pairs (i, j) where i is from [1, 2, 3] and j is from [4, 5, 6].
# pairs = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6]]
# print(pairs)


# Miscellaneous
# Filter Palindromes:
# From a list of strings, filter out the palindromes using a comprehension.
# Example: Input ['madam', 'racecar', 'hello', 'world'] → Output ['madam', 'racecar']
# words = ['madam', 'racecar', 'hello', 'world']
# palindromes = [word for word in words if word == word[::-1]]
# print(palindromes)
# Flatten a Nested List:
# Write a comprehension to flatten a list of lists.
# Example: Input [[1, 2], [3, 4], [5, 6]] → Output [1, 2, 3, 4, 5, 6]
# list = [[1,2],[3,4],[5,6]]
# flattened = [item for sublist in list for item in sublist]
# print(flattened)

##############################################
###########################################

# Count Words Starting with 'A':
# From a given list of words, count how many words start with the letter 'A'. Use a comprehension to first filter the list.
# words = ['apple', 'banana', 'avocado', 'apricot', 'grape']
# count = len([word for word in words if word.lower().startswith('a')])
# print(count)
# Challenge Questions
# FizzBuzz:
# Write a comprehension to generate the FizzBuzz sequence for numbers from 1 to 30:

# Replace multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
# Generate a Pascal Triangle Row:
# Using a nested comprehension, generate the nth row of Pascal's triangle.

