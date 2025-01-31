# age = int(input("enter your adhar card wala age:- "))
# if age <18 :
# #     print("please wait few more years")
# # elif age >=18 and age <30:
# #     print ("you can apply")
# # elif age>=30:
# #     print("cant apply")
# # else:
# #     ("enter your real age ")

# # marks = int(input("enter your marks:-"))
# # if marks >80:
# #     print("distingtion")
# # elif marks >=60  and marks<=80:
# #     print("first class")
# # elif marks >=45 and marks <60:
# #     print("second class")
# # elif marks<45:
# #     print("failed")
# # else:
# #     print("enter your valid marks")

# # str1= input("enter a string:-")
# # new_str = len(str1)
# # if new_str>5: 
# #     print("big string")
# # elif new_str>10 and new_str<15:
# #     print("very big string")
# # elif new_str>15:
# #     print("very very big string")
# # elif new_str==5:
# #     print("good string")
# # elif new_str<5:
# #     print("small string")
# # else:
# #     print("please enter a string next time:-")
# # take two input from the user do the multipilication between 
# num1 = int(input("enter your number: "))
# num2=int (input("enter your second number: "))
# total = num1*num2

# if total==100:
#     print("total hundred")
# elif total<100:
#     print("total is lesser than hundred")
# else :
#     print("answwr is greater than hundred")
    
# take a string as a input from user .if the intered string first charater is capital 
# and rest of the characters are small then print "title"
# char = input("inter any char:")
# if char.isupper():
#     print("upper")
# elif char.islower():
#     print("lower")
# # elif char.upper():
# #     print("upper")
# # elif char.istitle() and str2.strip():
# #     print("title")
# # elif char.capitalize():
# #     print("capital")
# str2 = input('Enter a string:- ')

# if str2.isupper():
#     print('Upper')
    
# elif str2.islower():
#     print('lower')
    
# elif len(char.split(' ')) > 1 and char.istitle():
#     print('title')
 
# elif len(char.split(' ')) == 1 and char.istitle():
#     print('capital')
# else:
#     print('Mixed')
# else:
#     print("capital")

str2 = input('Enter a string:- ')

if str2.isupper():
    print('Upper')
    
elif str2.islower():
    print('lower')
    
elif len(str2.split(' ')) > 1 and str2.istitle():
    print('title')
 
elif len(str2.split(' ')) == 1 and str2.istitle():
    print('capital')
else:
    print('Mixed')
    