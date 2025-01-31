# 1 . Check if marks of a subject are within range 0 - 100 .
# if - valid 
# else - invalid
# marks = int(input("enter student marks"))
# if marks>=0 and marks<=100:
#     print('valid')
# else:
#     print('invalid')
    
# Check if the person is eligible to work .
# age = int(input("enter your age"))
# if age>=18 and age <=68:
#     print("you can work")
# else:
#     print("you cant do this work beacause of your age")


#########################################################################################

# 1 . check if a statement has passed or failed , by taking marks in 3 subjects .
#  lets take marks of subjects ( maths , physics , chemistry ) marks are between 0 - 100 
# and passing marks should be above 45 
# physics = int(input("enter physics number"))
# maths = int(input("enter math number"))
# chemistry = int(input("enter chemistry number"))
# if physics>=45 and maths>=45 and chemistry>=45:
#     print("congratulations you passed the exam")
# else:
#     print("better luck next time")
# physics =int(input("inter physics number"))
# maths =int(input("inter maths number"))
# english =int(input("inter english number"))
# history =int(input("inter history number"))
# hindi =int(input("inter hindi number"))
# biology =int(input("inter biology number"))
# if physics>=45 and maths>=45 and english>=45 and history>=45 and hindi>=45 and biology>=45:
#     print("congratulation you passed the exam")
# else:
#     print("better luck next time")

############################################################################

# Check if a person is authorise for admin access 
# only admin can access the data by taking the user input .admins are ‘ John ‘ and ‘ smith’ 
# username =input("enter username")
# if username=="saurabh" or username=="bhavya":
#     print("authorise")
# else:
#     print("not authorise")
# username =input("enter username")
# password = input("enter your password")
# if username =='rahul' and password=='1234':
#     print("welcome")
# else:
#     print("nikal yaha se")

##############################################################################################

# Q ) check whether year is the leap year or not 
#  #a year have 365 days and 1/4 day , 4 quarter day makes one day and that will be added to 
# the feb month . Usually feb will have 28 days but in leap year( year % 400 == 0) it will have 29 
# days . Every fourth year will be the leap year . If the year is century( year %100 == 0 ) then it is not 
# leap year 
# year = int(input("enter year here"))
# # if year%100==0:
# if year%400==0:
#         print("leap year")
# else:
#         print("this is not leap year")


##############################################################################################

# Calculate discounted amount 
# amount <= 1000 —— 10%
# 1000 < amount <=5000 ——20%
# 5000 <amount <=10000 ——30%
# 10000 < amount ——50


##################################################################################################
# Take a day number and display day name 
# take any number and give it a day name . Its like switch case in other languages
# day = int(input("enter a number"))
# if day==1:
#     print("monday")
# elif day==2:
#     print("tuesday")
# elif day==3:
#    print("wednwsday")
# elif day==4:
#     print("thrusday")
# elif day==5:
#     print("friday")
# elif day==6:
#     print("saturday")
# elif day==7:
#     print("sunday")
# else:
#     print("please enter a valid number between 1 to 7,thank you😊")


####################################################################################333

# write a code for creating greater and small in two people
# ajay = int(input("enter first people age"))
# ranjay = int(input("enter second people age"))
# if ajay>=ranjay:
#     print("ajay is big brother")
# elif ajay<=ranjay:
#  print("ranjay is big brother")

# Basic Questions:

# Check Even or Odd
# Write a program to check whether a given number is even or odd.
# number = int(input("enter any number"))
# if number%2==0:
#     print("even number")
# else:
#     print("odd number")

# # Find Maximum of three Numbers
# number = int(input("add first number"))
# number1 = int(input("add first number"))
# if number>number1:
#     print("number is maximum")
# elif number<number1:
#     print("number1 is maximum")
# else:
#     print("given number is eual")

# Positive, Negative, or Zero
# Write a program to check if a number is positive, negative, or zero.
# num = int(input("enter any number "))
# if num>0:
#     print("number is positive")
# elif num<0:
#     print("number is negative")
# else:
#     ("number is zero")

# Pass or Fail
# Ask the user to input their marks (out of 100). If the marks are 40 or more, print "Pass"; otherwise, print "Fail."
# physics = int(input("enter marks of physics: "))
# maths = int(input("enter marks of physics: "))
# chemistry = int(input("enter marks of physics: "))
# if physics >= 40 and maths >= 40 and chemistry >= 40:
#     print("Congratulations, you passed the exam!")
# else:
#     print("Sorry, you did not pass the exam.")


# Check Leap Year

# Write a program to check if a given year is a leap year or not.

# Intermediate Questions:
# Check Vowel or Consonant
# char = input("enter a character").lower()
# if char in 'aeiou':
#     print("this character is a vowel")
# else:
#     print("this character is consonant")
# Write a program to check whether a given character is a vowel or a consonant.

# Grade Calculator
# Write a program that takes a student's score as input and prints their grade based on the following:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# marks = int(input("enter students marks here"))
# if marks >=90 and marks <=100:
#     print("A")
# elif marks >=80 and marks <=89:
#         print("B")
# elif   marks >=70 and marks <=79:
#         print("C")
# elif marks >=60 and marks <=69:
#                 print("D")
# elif marks <60:
#                     print("F")
# else:
#                     ("pleaser enter valuable number ")
# Divisibility Check
# Write a program to check whether a number is divisible by 5 and 11 or not.
# number = int(input("enter a number"))
# if number % 5==0 and number % 11==0:
#     print("this number is divisible by 5 and 11")
# else:
#     print("this number is not divisible by 5 and 11")
# Triangle Validity
# Write a program to check whether three given sides can form a triangle or not.

# Check Uppercase or Lowercase
# Write a program to check whether a given character is uppercase or lowercase.
# char = input("enter a char:")
# if char.isupper():
#     print("this character is uppercase character")
# elif char.islower():
#     print("this character is lowercase")
# else:
#     ("this character is no defined")
    

# Advanced Questions:
# Smallest of Three Numbers
# Write a program to find the smallest among three numbers.

# Electricity Bill Calculator
# Write a program to calculate the electricity bill based on the following rules:

# For the first 100 units: ₹5/unit
# For the next 200 units: ₹8/unit
# Beyond 300 units: ₹10/unit
# units = int(input("Enter electricity units consumed: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 300:
#     bill = (100 * 5) + (units - 100) * 8
# else:
#     bill = (100 * 5) + (200 * 8) + (units - 300) * 10
# print(f"Your electricity bill is ₹{bill}.")

# Login System
# Write a program to simulate a login system.# If the username is "admin" and the password is "12345", print "Login Successful."""
# Otherwise, print "Invalid Credentials."

# username = input("enter your uername :")
# password = input("enter your password here")
# if username =="saurabh@1" and password=="91234":
#     print("hey saurabh welcome to this amzing site")
# else:
#     print("nikal yaha se ")


# BMI Calculator
# Write a program that calculates Body Mass Index (BMI) and categorizes it as:
# Below 18.5: Underweight
# 18.5-24.9: Normal weight
# 25-29.9: Overweight
# 30 or above: Obese
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}.")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Quadratic Equation Roots
# Write a program to calculate and print the nature of the roots of a quadratic equation based on its discriminant.