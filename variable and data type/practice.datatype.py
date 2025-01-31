# Type Conversion:

# Write a program to:
# Convert an integer to a float.
# Convert a float to a string.
# Convert a string to an integer (if valid).
# Convert a list to a tuple and vice versa.

#convert an integer to a float.
# num_var = 10
# float_var = float(num_var)
# print(float_var)

# #convert a float to a string.
# float_var = 3.4567839
# str_var = str(float_var)
# print(str_var)

# Convert a integer to an string 
# int_var = "178"
# str_var = str(int_var)
# print(str_var)
# list1 = [7,8,9,67]
# print(dict(list1))
# Practice Questions string
# Basic
# Create a string and print its first and last character.
# str1 = [65,76,87,"saurabh"]
# print(str1[0])
# print(str1[-1])
# Write a program to count vowels in a given string. 
# str1 = "Python Programming"
# vowels = "aeiouAEIOU"
# count = 0

# for char in str1:
#     if char in vowels:
#         count += 1

# print("Number of vowels:", count)


# Check if a string is a palindrome.
# str1 = "madam"
# # if str1 == str1[::-1]:  # Compare string with its reverse
# # print("The string is a palindrome.")

# # else:
# print(str1[-1:0])  
# # print("The string is not a palindrome.")

# Reverse a string without using slicing.
# str1 = "Python"
# reversed_str = ""

# for char in str1:
#     reversed_str = char + reversed_str  # Prepend each character

# print("Reversed string:", reversed_str)

# Intermediate
# Write a program to find the most frequent character in a string.

# Replace all occurrences of a substring in a string with another substring.
# Split a string into words and count their frequency.
# Advanced
# Check if two strings are anagrams.
# Write a program to compress a string (e.g., "aaabbccc" → "a3b2c3").
# Implement a custom string search function without using built-in methods.
# If you need solutions or further explanations for these questions, let me know! 


########################## PRACTICE LIST IN PYTHON  ########################################
# Create a list with the numbers 1 to 10. Access the first, last, and a middle element from the list.
# list1 = [76,87,98,74,83]
# print(list1[0])
# print(list1[-1])
# print(list1[len(list1) // 2])

# Add the number 11 to the end of the list and 0 to the beginning.
# list1.append(11)
# print(list1)

# list1.insert(0,8)
# print(list1)
# Remove the number 5 from the list using both remove() and pop() methods.
# list1.remove(65) 
# print(list1)

# list1.pop()
# print(list1)


# Check if the number 7 is present in the list.
# is_7present = 7 in list1
# print(is_7present)
# # Find the length of the list.
# print(len(list1))
# list2 =[1,2,3,45,88,6,7,8,9]
# Extract the first five elements of a list.
# print(list2[:5])

# Reverse the list using slicing.
# print(list2[-1::-2])
# # Extract every second element from a list starting from the second element.
# print(list2[0::2])
# Replace the middle element of the list with a new value.
# middle_index = len(list2) // 2
# print(middle_index)
# middle_insert = list2.insert(4,8)
# print(list2)
# list3 = [87,76,89,89,76]
# list4 = [4,5,6,3]
# concatenate two lists [1, 2, 3] and [4, 5, 6].
# concatenate = list3+list4
# print(concatenate)
# # Multiply a list [1, 2, 3] by 3.
# multiply = list3*3
# print(multiply)
# Sort a list in ascending and descending order.
# list3.sort(reverse=False)
# print(list3)
# list3.sort(reverse=True)
# print(list3)
# Write a program to remove duplicates from a list.
# unique_numbers = list(set(list3))
# print(list3)
# Create a list of tuples where each tuple contains a number and its square (for numbers 1 to 10).

#################################################################################################################

# Access the element 5 from the nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[5])
# Flatten the nested list [[1, 2, 3], [4, 5], [6, 7, 8, 9]] into a single list.
# Write a program to transpose a 2D list.


########################################################################################3
list5 =[8,9,4,5,5,3,4,9,34,56]
# Find the maximum and minimum values in a list of numbers.
# print(max(list5))
# print(min(list5))

# Create a program to find the sum and average of a list of numbers.
# List of numbers

# Calculating sum and average
total_sum = sum(list5)
average = total_sum / len(list5)
print(total_sum)
print(average)

# Write a function that takes a list and returns a new list with all elements doubled.

# Find the index of a specific element in the list.
# List of numbers

# Finding the index of a specific element, say 30
index_of_element = list5.index(34)
print("Index of 30:", index_of_element)

# Create a program that rotates a list by n positions to the right.