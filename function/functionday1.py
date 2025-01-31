# create a function 
# def greet():
#     print("good morning! ")
# # call a function
# greet()
# user defined functions:-
# num1= int(input('enter a number:'))
# num2 = int(input('enter a number:'))
# def addition(a,b):
#     print(a+b)
# addition(num1,num2)
    
#rite a function which will provide square of number 
# num1 = int(input("enter number:"))
# def square(a):
#     print(a ** 2)
#     square(num1)
# take user into number and divide into .......and print the reminder.
# num = int(input("enter a number: "))
# def mod_of_num(a):
#     print(a % 2)
    
# mod_of_num(num)

# create a function which with do a floor division and normal division ..........print 
# num1=int(input("enter a number:-"))
# num2=int(input("enter a number:-"))
# def division_of_num(x,y):
#   print(x/y)
#   print(x//y)
# division_of_num(num2,num2)
# take 2 number from user and comapre them and print the largest number
# num1=int(input("enter a number:-"))
# num2=int(input("enter a number:-"))
# def compare_of_num(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# compare_of_num(num1,num2)

# num1=int(input("enter a number:-"))
# num2=int(input("enter a number:-"))
# def minimum_num(a,b):
#     print(a if a<b else b)
# minimum_num(num1,num2)

# take a input from user and convert into reverse.
# str1 = input("Enter a string: ")

# def reverse_of_str1(a):
#     print(a[::-1])

# reverse_of_str1(str1)
 
 # write a function ways to display only even number in provided range.
# num1=int(input("enter a number:-"))
# num2=int(input("enter a number:-"))
# def display_even_numbers(x, y):
#     for num1 in range(x, y+1):
#         for num2 in range(x, y+1):
#          if num % 2 == 0:
#             print(x,y)
#             display_even_numbers(num1,num2)
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# def display_even_numbers(x, y):
#     for i in range(x, y):
#         if i % 2 == 0:
#             print(i)

# display_even_numbers(num1, num2)

# print take a string from user and print only vowels.
# str1 = input("Enter your string: ")
# vowels = 'aeiouAEIOU'
# def find_vowels(a):
#     for char in a:
#         if char in vowels:
#             print(char)

# find_vowels(str1)
#print a prime number with the help of prime number in between from 4,100.

########################################################################################
##########################################################################################

 
 
 
 
 ################################################################################################
 ###################################################################################################
 ##################################################ARUGUMENT######################################

#take a argument find the number divisible by 5 and 3 .
# def lowest_num_divisible_by_5(*args):
#     list_of_num=[]
#     for i in args:
#         if i %3 == 0 and i % 5 == 0:
#             list_of_num.append(i)
#         else:
#             pass
        
#         print(min(list_of_num))
        
#         lowest_num_divisible_by_5(13,34,45,67,89,54,768,44,3,455,333)
            
#take string and print the string which length is greater
    
# def print_longer_string(*args):
#     if args:
#         str1 = max(args,key=len)
#         print(str1)
#     else:
#         print("please provide valid string")
# print_longer_string("Hello", "saurabh", "kaundaiya", "Progrram")

#########################################variable length keyword argument##################################
# def summation(**kwargs):
#   print(**kwargs)
#   print(type(kwargs))


# summation(a=1,b=2,c=5,d=4)
  
#########################################
#write a function to find out take 3 arugment and find maximum and minimum and print them.
# def find_max_mini(**kwargs):
#     if kwargs:
#          num = max(kwargs,key=len)
#     print(num)
#     if kwargs:
#         num1 = min(kwargs,key=len)
#         print(num1)
        
# find_max_mini(x=7,y=9,z=17)
  
# def find_max_mini(**saurabh):
#     if saurabh:
#         max_value = max(saurabh.values())  
#         min_value = min(saurabh.values())  
#         print(f"Maximum: {max_value}")
#         print(f"Minimum: {min_value}")
#     else:
#         print("please provide some arguement")
# find_max_mini(x=7, y=9, z=17)

# write a function to find out the right angle trangle area.
