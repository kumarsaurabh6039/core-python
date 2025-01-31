# -----------------------------------COMPREHENSIONs-----------------------------------------------
# Key Benefits of Comprehensions
# Conciseness: Reduce multiple lines of code into one line.
# Readability: Clear and intuitive when used properly.
# Performance: Faster than equivalent loops for small to medium-sized data sets.
# Flexibility: Support mapping, filtering, and complex nested structures.


# # List Comprehensions:-
# 1)squares = [x**2 for x in range(10)]
# squares = [i**2 for i in range(10)]
# print(squares)
# # 2)evens = [ X for x in range(10) if x % 2 == 0]
# evens = [i for i in range(10) if i % 2==0]
# print(evens)
# 3)words = ["python", "comprehension", "example"]
# uppercase_words = [word.upper() for word in words]
# student_list = ["rohan","ashutosh","ayush"]
# uppercase = [i.upper() for i in student_list]
# print(uppercase)
#  months_in_small = ['january', 'february', 'march', 'april', 'may'] 

# months_in_upper = [i.upper() for i in months_in_small]
# print(months_in_upper)

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

# 5)list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# cartesian_product = [(x, y) for x in list1 for y in list2]


# # Tuple Comprehensions:-
# Similar to list comprehension, but it creates a generator object instead of a list. Useful for large data sets as it computes items lazily (on demand).
# squares_gen = (x**2 for x in range(10))


# # Dictionary comprehensions:-
# 1)squares_dict = {x: x**2 for x in range(5)}
# filtered_dict = {x: x**2 for x in range(10) if x % 2 == 0}

# 2)original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# filtered = {key: value for key, value in original.items() if value % 2 == 0}

# 3)original = {'a': 1, 'b': 2, 'c': 3}
# swapped = {value: key for key, value in original.items()}

# 4)keys = ['name', 'age', 'city']
# values = ['Alice', 25, 'New York']
# combined = {key: value for key, value in zip(keys, values)}

# 5)numbers = range(1, 6)
# result = {x: ('even' if x % 2 == 0 else 'odd') for x in numbers}


# # Set Comprehensions:-
# unique_squares = {x**2 for x in range(-5, 6)}



# ******************************COMPLEX USE CASES*******************************************

# matrix = [[x * y for x in range(1, 4)] for y in range(1, 4)]
# filtered = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]