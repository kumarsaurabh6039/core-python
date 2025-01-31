# datatypes
# conditional startements
# control statements
# Operators
# comprehensions
# functions
# File Handeling

#######################
# try:
#     user_input = input("Enter a string to reverse: ")

#     if not user_input.strip():
#         raise ValueError("Input cannot be empty or whitespace only.")
#     reversed_input = user_input[::-1]
#     print(f"Reversed string: {reversed_input}")

# except ValueError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


# Recap of functions
# Error and Exception Handling
# lambda
# map, reduce, filter
# Regex
#####################

# def evenNums(a, b):
#     for i in range(a, b):
#         if i % 2 == 0:
#             print(i)
#         else:
#             pass

# evenNums('a', 'b')

# try:
#     lower_limit = int(input('Enter lower limit of range: '))
#     upper_limit = int(input("Enter upper limit of range: "))

#     for i in range(lower_limit, upper_limit):
#         if i % 2 == 0:
#             print(i)
            
#         else:
#             pass
# except ValueError as msg:
#     print(msg)
    

    
# ValueError: invalid literal for int() with base 10: 'a'
# IndexError: string index out of range
# try:
#     str1 = input('Enter a string: ')
#     print(str1[1])
# except IndexError as e:
#     print(e)

# write a programme which takes two inputs for division and returns division of it.
# handle zerodivisionerror gracefully.
# ZeroDivisionError: division by zero
# try:
#     numerator = int(input('Enter a numerator: '))
#     denominator = int(input("Enter a denominator: "))
#     print(numerator / denominator)
# except:
#     print("Please enter a value greater than 0")
    
    
# try:
#     numerator = int(input('Enter a numerator: '))
#     denominator = int(input("Enter a denominator: "))
#     print(numerator / denominator)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError  as e:
#     print(e)
    
  
# num1 = int(input("Enter a numerator: "))
# num2 = int(input("enter a denominator: "))
# if num2 != 0:
#     print(num1 / num2)

# else:
#     print(-1)


# print('w' / 2)  # TypeError
# print(int('w'))


########################################################

# def division(a, b):
#     try:
#         ans =  a / b
        
#     except ZeroDivisionError as e:
#         return e
    
#     else:
#         return ans
    
# a = division(12, 3)
# print(a)

# b = division(5, 0)
# print(b)

# print(3 + 't')

# def addition(x, y):
#     try:
#         ans = x + y
        
#     except TypeError as e:
#         return e
#     else:
#         return ans
    
    
# a = addition(12, 23)
# print(a)

# b = addition(12, 'sameer')
# print(b)

# tup1 = ('item')
# tup1 += tup1 + 5   
# def addItems(item):
#     try:
#         tup1 = (item)
#         tup1 += 5
        
#     except TypeError as e:
#         return e
#     else:
#         return tup1
    
    
# a = addItems('23')
# print(a)

# write a function which does subtraction of two arguments of type numbers.
# handle error. (own error msg)

# def subtract(a, b):
#     try:
#         ans = a - b
#     except:
#         return "Please enter only numeric values."
    
#     else:
#         return ans
    
    # finally:
    #     return "Programme executed successfully"
    
    
# a = subtract(12, 'abc')
# print(a)


# def subtraction():
#     try:
#         num1 = int(input("Enter a first number: "))
#         try:
#             num2 = int(input("Enter a second number: "))
#         except:
#             raise ValueError('value error')
#     except:
#         raise ValueError('Value error')
#     else:
#         print(num1 - num2)
#     finally:
#         print("Programme Executed successfully.")
     
# print(subtraction())

# print((34+5j) % 5)

# if not complex first input --> value err
# if not integer scond input --> value error
# complex % int occurs --> type error.

# write a function which takes input as age.

# class NegativeAgeError(Exception):
#     pass


# def giveAge(age):
#     if age < 0:
#         raise NegativeAgeError("PLease Enter a positive Number.")
    
#     elif age < 10:
#         print('Kid')
        
#     elif age > 10 and age < 25:
#         print('young')
        
#     elif age > 25 and age < 50:
#         print('Adult')
        
#     else:
#         print('Old')
        
# myage = int(input("Enter age: "))  
# try:     
#     giveAge(myage)
# except NegativeAgeError as e:
#     print(e)
    
    
    
# Write a programme which when customer debits the amount from 
# account it will debit it and give remmaining balance.
# but as per bank policy customer can not withdraw a balance more 
# than available balance.
# second rule  of back is have to maintain minnimum 5000 rs 
# balance in account
# Handle the exception for that create used defined MinimumBalanceError.



#########################
# wap which is handle exception ....take two input from user and do multiplication on it .


# try:
#     num1=int(input("enter a number: "))
#     num2=int(input("enter second number: "))
#     print(num1*num2)
# except:
#     print("please enter integer value")
#find even number in range and if .
# try:
#     start=int(input("enter starting number: "))
#     end=int(input("end of number: "))
#     for i in range(start,end):
#         if i % 2==0:
#             print(i)
# except:
#     print("please enter integer value for finding even number in range")

# take a input from a user and reverse as a string a handle exception tool.
# try:
#     string = input("Enter a string to reverse: ")

#     if not string.strip():
#         raise ValueError("Input cannot be empty or spaces.")
#     reversed_input = string[::-1]
#     print(f"Reversed string: {reversed_input}")

# except ValueError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"An unexpected error: {e}")

#############################################
###############################################
# def division(a, b):
#     try:
#         division =  a / b
        
#     except ZeroDivisionError as e:
#         return e
    
#     else:
#         return division
    
# a = division(12, 6)
# print(a)

##################################
#########################################
# 1. Basic Try-Except
# Write a Python function that takes a number as input and divides 100 by the number. Use a try-except block to handle the case where the number is zero and print an error message.
# def divide(a):
#     try:
#         division=100/a
#         print(division)  
#     except ZeroDivisionError:
#         print("can not divide by zero")
# divide(0)
     
    
        
# 2. Handling Multiple Exceptions
# Create a program that reads a file. If the file does not exist, handle the FileNotFoundError. If the file is empty, handle the IsADirectoryError. Make sure that the appropriate error message is printed for each error type.

# 3. Catching Specific Exception Types
# Write a function that takes two arguments: a numerator and a denominator. Try to divide them and catch both ZeroDivisionError and TypeError exceptions. Print a specific message depending on the exception raised.
# def divide():
#     try:
#         numerator = int(input("Enter numerator: "))
#         denominator = int(input("Enter denominator: "))
#         division = numerator / denominator
#         print(f"The result of {numerator} divided by {denominator} is: {division}")
    
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero!")
#     except ValueError:
#         print("Error: Please enter integer values.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
# divide()

           
           
# 4. Using Else with Try-Except
# Write a function that takes two numbers, divides the first by the second, and prints the result. If no exception is raised, print "Division successful". If an exception occurs, print "Error occurred during division". Use an else block to print the success message.
# Write a function that takes two numbers, divides the first by the second, and prints the result. If no exception is raised, print "Division successful". If an exception occurs, print "Error occurred during division". Use an else block to print the success message.
# def division():
#     try:
#         first_num=int(input("enter the first number: "))
#         second_num=int(input("enter the second number: "))
#         result=first_num/second_num
#         print(f"division of {first_num} / {second_num} = {result}")
#     except Exception as msg:
#         print(msg)
#     else:
#         print("your work is done ,go to hell")
# division()
    
    
# 5. Raising Exceptions
# Create a function that takes an integer and checks if it is negative. If it is negative, raise a ValueError with a message: "Negative numbers are not allowed!". Otherwise, return the number.
# def find_num():
#     try:
#         num = int(input("Enter a number: "))
#         if num < 0:
#             raise ValueError("Negative numbers are not allowed!")
#         else:
#             print(num)
#     except ValueError as e:
#         print(e)

# find_num()

    
        

# 6. Finally Block
# Write a program that opens a file, writes some content to it, and then ensures the file is closed properly using a finally block.
# try:
#     file = open("example.txt", "w")
    
#     file.write("Hello, this is a test file.\n")
#     file.write("Writing some more content to it.")
    
# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     if 'file' in locals() and not file.closed:
#         file.close()
#         print("File is closed.")
# Write a programme which when customer debits the amount from 
# account it will debit it and give remmaining balance.
# but as per bank policy customer can not withdraw a balance more 
# than available balance.
# second rule  of back is have to maintain minnimum 5000 rs 
# balance in account
# Handle the exception for that create used defined MinimumBalanceError.
# def division():
#     try:
#        a=int(input("enter a number: "))
#        b=int(input("enter a number: "))
#        print(f"{a}/{b}={a/b}")
#     except ZeroDivisionError:
#         print("given number is not divided by 0")
# division()

##############################################3
##################################################
# def get_division(numerator:int,denominator:int):
#     try:
#         ans=numerator//denominator
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print(ans)
#     finally:
#         print("programme has run successful.")
# get_division(5,2)
#########################################################3
#############################################################
# try:
#     num1=int(input("enter first number: "))
#     try:
#         num2=int(input("enter a number: "))
#     except:
#         raise ValueError                #esko pura krna hai
# except 

##########################
#######################
# def mathematics_operation():
#     exp = input("Enter expression: ")

#     if '+' in exp:
#         num1, num2 = exp.split('+')
#         print(int(num1) + int(num2))
#     elif '-' in exp:
#         num1, num2 = exp.split('-')
#         print(int(num1) - int(num2))
#     elif '*' in exp:
#         num1, num2 = exp.split('*')
#         print(int(num1) * int(num2))
#     elif '/' in exp:
#         num1,num2 = exp.split('/')
#         print(int(num1)/ int(num2))
#     else:
#         print("Invalid expression")

# mathematics_operation() 

###################################################
#######################################################
list1 = [125, 250, 375, 400, 555, 690]
# ind = int(input('Enter index '))
# print(list1[ind])
##########################
# try:
#     ind = int(input('Enter index '))
#     print(list1[ind])
    
# except:
#     print("Entered incorrect index")
#########################

# try:
#     print(list1[ind])
#     print('Successful')
# except:
#     print('Error')
##########################

# try:
#     ind = int(input('Enter index '))
#     print(list1[ind])
#     print('Successful')
    
# except ValueError:
#     print('Value Error')
    
# except TypeError:
#     print('Type Error')
    
# except IndexError:
#     print('Index Error')

# except (ValueError, TypeError, IndexError):
#     print('Error')

# except (ValueError, TypeError, IndexError) as msg:
#     print(msg)

########################################

# def divide(a, b):
#     if b != 0:
#         return (a // b)

#     else:
#         return -1
       
       
# a = int(input("Enter value of a:"))
# b = int(input('Enter value of b:'))

# c = divide(a, b)
# if c == -1:
#     print('Zero Division Error')
# else:
#     print(c)
    
#######################################################

# def divide(a, b):
#     if b != 0:
#         return a // b
#     else:
#         raise ZeroDivisionError
    
    
# x = int(input("Enter value of x: "))
# y = int(input('Enter value of y: '))

# try:
#     z = divide(x, y)
#     print(z)
    
# except:
#     print('Zero Division error')
    
    
#########################################

# def get_division(numerator, denominator):
#     try:
#         ans = numerator // denominator  
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print(ans)    
#     finally:
#         print('programme has run successfully.')
# get_division('a', 'd')

# def get_addition():
#     try:
#         num1 = int(input("enter first number: "))
#         try:
#             num2 = int(int(input("Enetr second number: ")))
#         except:
#             raise ValueError('Please enter a number')
#     except ValueError as e:
#         print(e)
#     else:
#         ans = num1 +  num2
#         print(ans)
#     finally:
#         print("Programme executed successfully..")
                
# get_addition()

#######################################################

# class NegativeAgeError(Exception):
#     pass

# def ageGroup(age):
#     if age < 0:
#         raise NegativeAgeError('Age should not be negative')
    
#     elif age >= 0 and age < 13:
#         print('kid')
        
#     elif age >= 13 and age < 25:
#         print('Teen')
        
#     elif age >= 25 and age < 50:
#         print('adult')
        
#     else:
#         print('old')
        
    
# myAge = int(input("Enter your age: "))

# try:
#     ageGroup(myAge)
    
# except NegativeAgeError as e:
#     print(e)
    
# finally:
#     print('code executed successfully')
    

#################################################################
# class AccountBalanceException(Exception):
#     pass

# class NoNegativeAmountException(Exception):
#     pass

# class NoAvailableBalance(Exception):
#     pass


# TotalBalance = 19000

# def passbook(amount):
#     if not isinstance(amount, int):
#         raise TypeError ("Please enter Numeric amount")
#     elif amount < 0:
#         raise NoNegativeAmountException('Amount Should be Greater than Zero,')
    
#     elif amount > TotalBalance:
#         raise NoAvailableBalance("Entered amount is greater than total balance")
    
#     elif (TotalBalance - amount) < 5000:
#         raise AccountBalanceException("Debitting Entered Amount can voilet minimum balance rule")
    
#     else:
#         print(f'Amount has been Debitted Successfully.\n Available  amount is {TotalBalance - amount}')

# try:
#     passbook('apple')
    
# except NoAvailableBalance as e:
#     print(e)
# except NoNegativeAmountException as e:
#     print(e)
    
# except TypeError as e:
#     print(e)
    
# except AccountBalanceException as e:
#     print(e)
   
# finally:
#     print('Code has been excuted successfully') 

#############################################################

# class ExpressionException(Exception):
#     pass

# class NoGapException(Exception):
#     pass

# def giveExpression(exp):
#     list1 = exp.split()
#     if len(list1) < 3:
#         raise NoGapException("Maybe you havent entered the gap between numbers and operator Ex: 10 + 12")
    
#     elif list1[1] == '+' or list1[1] == '-' or list1[1] == '*' or list1[1] == '/' or list1[1] == '//':
#         if list1[1] == '+':
#             res = int(list1[0]) + int(list1[2])
        
#         elif list1[1] == '-':
#             res = int(list1[0]) - int(list1[2])
            
#         elif list1[1] == '*':
#             res = int(list1[0]) * int(list1[2])
            
#         elif list1[1] == '/':
#             if int(list1[0]) != 0 and int(list1[2] != 0):
#                 res = int(list1[0]) / int(list1[2])
#             else:
#                 raise ZeroDivisionError
            
#         elif list1[1] == '//':
#             if int(list1[0]) != 0 and int(list1[2] != 0):
#                 res = int(list1[0]) // int(list1[2])
#             else:
#                 raise ZeroDivisionError
        
#         return res
#     else:
#         raise ExpressionException('Enter Proper Arithmetic Expression')

# try:
#     express = input("enter the expression: ")
#     a = giveExpression(express)
        
# except ExpressionException as e:
#     print(e)
# except NoGapException as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print(a)

# finally:
#     print('Code Executed Sufccessfully')
    
# #############################
# ############################
# # class ExpressionException(Exception):
# #     pass

# # class NoGapException(Exception):
# #     pass
# # def mathematics_operation():
#     # try:
        