# [20-12-2024 19:30] Shiva Sir: Write a program that takes a number as input and prints:
# "Fizz" if the number is divisible by 3.
# "Buzz" if the number is divisible by 5.
# "FizzBuzz" if the number is divisible by both.
# Otherwise, print the number itself.
# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
# elif number % 3 == 0:
#         print("Fizz")
# elif number % 5 == 0:
#         print("Buzz")
# else:
#         print(number)

#######################################################################################
########################################################################################

# [20-12-2024 19:30] Shiva Sir: Write a program to calculate a student's grade based on the following conditions:
# Score >= 90: Grade A
# Score >= 80: Grade B
# Score >= 70: Grade C
# Score < 70: Grade F
# marks = int(input("Enter your marks:"))
# if marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("Grade B")
# elif marks>=70:
#     print("Grade C")
# else:
#     print("Grade F")
    #################################################################################################
    
    #################################################################################################
    
# [20-12-2024 19:31] Shiva Sir: Write a program that calculates the fare of a taxi based on these conditions:
# First 5 km: ₹10 per km
# Next 10 km: ₹8 per km
# Beyond 15 km: ₹6 per km
# distance = int(input("enter distance:"))
# if distance<5:
#     print(distance*10)
# elif distance>5 and distance<=10:
#     print(distance*8)
# elif distance >15:
#     print(distance*6)

####################################################################################
#################################################################################333

# [20-12-2024 19:31] Shiva Sir: A company gives a bonus based on performance:
# Sales >= ₹50,000: 10% bonus
# Sales >= ₹30,000 but < ₹50,000: 5% bonus
# Sales < ₹30,000: No bonus Write a program to calculate the bonus.

# [20-12-2024 19:31] Shiva Sir: Implement a program to check if a user is eligible for a loan. Conditions include:
# Age >= 21
# Minimum monthly salary of ₹25,000
# No outstanding loans
# age = int(input("enter your age: "))
# salary = int(input("enter emloyee salary here: "))
# loan_dues = int(input("enter your loan dues: "))
# if age>=21 and salary>25000 and loan_dues ==0:
#     print("congratulation ! u r eligible for this loan")
# else:
#     print("nikal yaha se bhikhari dues clr kr pahle")
    
######################################################################################
##########################################################################################


# [20-12-2024 19:32] Shiva Sir: Traffic Light System: Write a program that simulates a traffic light.
# Based on the input (red, yellow, green), the program should display the appropriate action (e.g., "Stop", "Get Ready", "Go").
# light_colour = input("enter a color(red,yellow,green):")
# # colour_type=("red")
# if light_colour == "red":
#     print("stop")
# elif light_colour=="yellow":
#     print("get ready")
# elif light_colour=="green":
#     print("Go")
# else:
#     print("please enter (red,green,yellow) any of these")
    
# [20-12-2024 19:33] Shiva Sir: Bank ATM: Write a program that checks the balance of an account
# and processes a withdrawal request only if sufficient funds are available.

# balance = 8000
# while True:   # hint lekar krte hai esse 
#  withdraw = int(input("enter a balance : "))
#  if withdraw<balance:
#      print("wait a minute your amount is ready for withdraw")
#      break
#  else:
#      withdraw-=balance
#      print("your available :",balance)
    
# [20-12-2024 19:33] Shiva Sir: Electricity Bill Calculator: Create a program to calculate an electricity bill based on these slabs:
# First 100 units: ₹5 per unit
# Next 200 units: ₹8 per unit
# Beyond 300 units: ₹10 per unit

# [20-12-2024 19:33] Shiva Sir: Library Fine Calculator: Write a program that calculates the fine for a library book based on the number of overdue days:
# 1–5 days: ₹2 per day
# 6–10 days: ₹5 per day
# Beyond 10 days: ₹10 per day
# library= int(input("enter day of using :"))
# if library<=5:
#  print(library*2)
# elif library>=5 and library<=10:
#     print(library*5)
# elif library>10:
#     print(library*10)
    
# [20-12-2024 19:33] Shiva Sir: Shipping Cost Calculator: Write a program to calculate shipping costs:
# Orders over ₹1000: Free shipping
# Orders between ₹500 and ₹1000: ₹50 shipping fee
# Orders below ₹500: ₹100 shipping fee
# Input: Order amount
# order_amount = int(input("Enter the order amount: "))
# if order_amount > 1000:
#     shipping_cost = 0  
#     print("free shipping")
# elif order_amount >= 500:
#     shipping_cost = 50  
#     print("50 rupaye de or shipping free hai")
# else:
#     shipping_cost = 100 
#     print("100 rupaye de shipping free hai")

# # Output: Display the shipping cost
# print(order_amount)
# print(shipping_cost)
# print(order_amount + shipping_cost)
#############################################################################################
#############################################################################################

# [20-12-2024 19:34] Shiva Sir: Exam Result System: Write a program to classify a student's 
# grade based on their marks:
# = 90: Excellent

# 75–89: Very Good
# 50–74: Pass
# < 50: Fail
# marks =int(input("enter your marks:" ))
# if marks == 90:
#     print("excellent")
# elif marks>=75 and marks<=89:
#     print("very good")
# elif marks>=50 and marks<=74:
#     print("pass")
# elif marks<50:
#   print("fail")
# else:
#     ("enter your real marks")
    
# [20-12-2024 19:34] Shiva Sir: Scholarship Eligibility: Check if a student is eligible for
# a scholarship based on these conditions:
# Family income < ₹2,50,000
# Marks >= 85%
# No backlogs in previous semesters

# student_family_encome =int(input("inter your family income: "))
# student_marks = int(input("enter your marks: "))
# backlogs = int(input("if you have no backlog then enter 0 otherwise enter 1: "))
# if student_family_encome<250000 and student_marks>=85% backlogs==0:
#     print("you are eligible for scholarship ")
# else:
#     print("sorry! you are no eligible")



# [20-12-2024 19:34] Shiva Sir: Clothing Suggestion: Write a program that suggests clothing based on the temperature:
# Temperature > 30°C: "Wear light cotton clothes."
# Temperature 20°C–30°C: "Wear comfortable clothes."
# Temperature < 20°C: "Wear warm clothes."
# [20-12-2024 19:34] Shiva Sir: Travel Planner: Write a program to suggest a mode of travel based on distance:
# Distance < 5 km: "Walk"
# 5–20 km: "Bike"
# 20–100 km: "Car"
# 100 km: "Flight"
# [20-12-2024 19:35] Shiva Sir: BMI Calculator: Write a program to calculate BMI and display the health category:
# BMI < 18.5: "Underweight"
# 18.5–24.9: "Normal weight"
# 25–29.9: "Overweight"
# = 30: "Obesity"



# The formula for calculating body mass index (BMI) is BMI = kg/m2, where kg is weight in kilograms and m2 is height in meters squared.
# [20-12-2024 19:48] Shiva Sir: Loop Questions:-

# Countdown Timer: Write a program that counts down from 10 to 1 and then prints "Blast off!"

# Factorial: Write a program to calculate the factorial of a given number.

# Shopping Cart Total: Given a list of item prices in a shopping cart, calculate and print the total bill.

# Character Count: Write a program to count the occurrences of each character in a string.

# *
# **
# ***
# ****
# *****
# Write a program to generate this pattern using nested loops.
# [20-12-2024 19:49] Shiva Sir: Weather Data Analysis: Write a program to analyze daily temperature data (a list of temperatures) and:
# Count the number of hot days (temp > 30°C).
# Calculate the average temperature.
# [20-12-2024 19:51] Shiva Sir: Bank Transactions: Given a list of transactions (deposits and withdrawals), calculate the final account balance starting from ₹10,000.
# [20-12-2024 19:51] Shiva Sir: Parking Lot Revenue: A parking lot charges:
# ₹20 for the first hour
# ₹10 for each additional hour Write a program to calculate the total revenue for a given list of parked durations.
# [20-12-2024 19:51] Shiva Sir: Discount on Bulk Orders: Write a program to calculate the total bill after applying discounts:
# 10% discount for quantities >= 10
# 20% discount for quantities >= 50
# 30% discount for quantities >= 100