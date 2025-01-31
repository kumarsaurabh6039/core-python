# Beginner Level
# Print Numbers from 1 to 10
# Write a for loop that prints the numbers from 1 to 10.
# for i in range(1,10):
#     print(i)
# Sum of Numbers in a List
# Write a for loop that calculates the sum of the numbers in the list: [2, 4, 6, 8, 10].
# numbers = [2, 4, 6, 8, 10]
# new_numbers = 0
# for num in numbers:
#     new_numbers+=num
#     print(new_numbers)
# Count Even Numbers in a List
# Given a list [1, 2, 3, 4, 5, 6, 7, 8, 9], write a for loop to count how many even numbers are in the list.
# list =[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in list:
#     if num%2==0:
#         print(num)
# Print Squares of Numbers
# Write a for loop that prints the square of each number in the list [1, 2, 3, 4, 5].
# list= [1, 2, 3, 4, 5]
# for num in list:
#         print(num**2)
# Find Maximum in a List
# Write a for loop to find the largest number in the list [10, 20, 4, 45, 99].
# list = [10, 20, 4, 45, 99]
# max_num = list[0]
# for num in list:
#     if num > max_num:
#         max_num = num
#         print(max_num)
    
# Intermediate Level
# Reverse a String
# Write a for loop to reverse the string "Hello, world!" and print the reversed string.
# string ="Hello, world!"
# for char in string:
#     print(string[::-1])
    
# Multiplication Table
# Write a for loop that prints the multiplication table for the number 5 (from 5x1 to 5x10).
# for i in range(1,11):
#     print(i*5)
# Fibonacci Sequence
# Write a for loop that prints the first 10 numbers of the Fibonacci sequence.

# Nested For Loop (Matrix Print)
# Write a program using a for loop inside another for loop to print the following 2D matrix:

# Copy code
# 1 2 3
# 4 5 6
# 7 8 9

# Sum of Elements in a Nested List
# Given a nested list [[1, 2], [3, 4], [5, 6]], write a for loop to sum all the elements inside the nested list.

# Advanced Level
# Prime Numbers
# Write a for loop that prints all prime numbers between 1 and 100.

# Count Vowels in a String
# Write a for loop that counts the number of vowels in the string 
# "The quick brown fox jumps over the lazy dog".
# string = "The quick brown fox jumps over the lazy dog"
# vowels = "aeiouAEIOU"
# vowel_count = 0
# for char in string:
#     if char in vowels:
#         vowel_count += 1
# print(vowel_count)
        
        

# Find Common Elements in Two Lists
# Write a for loop that finds and prints the common elements between 
# the lists [1, 2, 3, 4, 5] and [3, 4, 5, 6, 7].
# list1= [1, 2, 3, 4, 5]
# list2 =[3, 4, 5, 6, 7]
# list3=[]
# for item in list1:
#     if item in list2:
#         list3.append(item)
#         print(list3)
# Generate a Pattern
# Write a for loop to print the following pattern:
# *
# **
# ***
# ****
# *****
# for i in range(1, 6):
#     print('s' * i)
# Multiples of a Number
# Write a for loop that prints all the multiples of 7 between 1 to 100:
# for i in range(1,100):
#     if i %7==0:
#         print(i)