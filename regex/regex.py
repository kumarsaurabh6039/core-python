import re

# match function
# checks for a match only at the beginning of the string.
# returns a match object if the pattern matches, else none.

# string1 = re.match(r'good', 'good morning!')
# print(string1)

# string2 = re.match(r'hello', 'good morning!')
# print(string2)

# with open('string3.txt', 'w+') as string3:
#   string3.writelines([
#     'im writing some lines in string3 file\n',
#     'this is it'
#   ])
#   string3.seek(0)
#   stringread = string3.read()
# print(stringread)
# string4 = re.match(r'im', stringread)    # it only search only starting value of the string
# print(string4)
# string3.close()


# search function
# searches the entire string for a match
# returns the first occurences of the match

# def search_string(string1, input_str):
#   string6 = re.search(r'input_str', string1)
#   print(string6)

# with open('string3.txt', 'w+') as string5:
#   string5.writelines([
#     'im writing some lines in string3 file\n',
#     'in this we use search function\n',
#     'rather than match function\n',
#     'because match function searches only beginning of the string\n'
#   ])
#   string5.seek(0)
#   stringread1 = string5.read()
# string5.close()

# inputstr = input("Enter a string:- ")
# search_string(stringread1, inputstr)


# first write function, take three arguments [filename, data, pattern]
# def search_input(file_name, file_data, pattern):
#   file_name1 = file_name.split('.')[0]
#   file_name1 = open(file_name, 'w+')
#   file_name1.writelines(file_data)
#   file_name1.seek(0)
#   file_content = file_name1.read()
#   file_name1.close()
#   search_input = re.search(rf'{pattern}', file_content)
#   print(search_input)

# data = 'im searching a word in this string'

# search_input('str1.txt', data, 'word')


# def searching_str(file_name, file_data, file_pattern):
#   file_name2 = file_name.split('.')
#   file_name2 = open(file_name, 'w+')
#   file_name2.writelines(file_data)
#   file_name2.seek(0)
#   file_read = file_name2.read()
#   file_search = re.search(rf'{file_pattern}', file_read)
#   print(file_search)
#   file_name2.close()

# data1 = [
#   'im adding some lines in this file\n',
#   'in this file i search for a word\n',
#   'if the word is there it will print the index of the word\n',
#   'otherwise it will prints none\n',
#   'it will search the word anywhere in the string\n',
#   'not like match function\n',
#   'match function search only first word of the string'
# ]

# searching_word = input("Enter a word to search:- ")
# searching_str('searchingInput.txt', data1, searching_word)


# write a function input from user as a number and find out the armstrong number is not?

# def armstrong_num(num):
#   num_str = str(num)
#   sum_powers = 0
#   temp_num = num
#   num_digits = len(num_str)


#   while temp_num > 0:
#     digit = temp_num % 10
#     sum_powers += digit ** num_digits
#     temp_num //= 10

#   if sum_powers == num:
#     return f"the {num} is armstrong number!"
#   else:
#     return f"the {num} is not armstrong number!"
  
# num = int(input("Enter a number:- "))


# print(armstrong_num(num))

# def armstrong_num(num):
#   num_str = str(num)
#   num_len = len(num_str)

#   total = 0

#   for i in num_str:
#     total += int(i) ** num_len

#   if total == num:
#     return f"the {num} is armstrong number!"
#   else:
#     return f"the {num} is not armstrong number!"

# num1 = int(input("Enter a number:- "))
# print(armstrong_num(num1))


# write a function and take a input from user and do fibonacci series
# def fibonacci_series(num1, num2):
#   sum = 0
#   length = int(input("Enter how many you want to do fibonacci:- "))
#   count = 0

#   print(num1)
#   print(num2)
#   while count != length:
#     sum = num1 + num2
#     print(sum)
#     num1 = num2
#     num2 = sum
#     count += 1

# num1 = int(input("Enter 1st number:- "))
# num2 = int(input("Enter 2nd number:- "))

# fibonacci_series(num1, num2)

# def fibonacci_series(num1, num2, length):
#   for i in range(length):
#     sum = num1 + num2
#     print(sum)
#     num1 = num2
#     num2 = sum

# fibonacci_series(7, 9, 4)

####################################
###################################


text = """Hello! This is a Python regex tutorial. Python is powerful!
User123, here are $5.00 items: Apples, Oranges, & Bananas!
example@domain.com, user@domain.org
Today is 09/01/2025. Tomorrow is 10/01/2025.
This   is  an   example with   multiple spaces.
Contact: Alice (123) 456-7890, Bob (987) 654-3210
Price: $20.50, Quantity: 20 items
https://www.example.com/path/to/page
[INFO] 2025-01-09 10:00:00 - Starting process
[ERROR] 2025-01-09 10:01:00 - Invalid user input
"""

# output = re.match('Hello',text)
# print(output)

# # /d --> only for single digit
# got1 = re.match('\d+', '13fg342345jhjhcvb45')
# print(got1)

# zetra1 = re.match('\d+', '1234fghj3hf1243')
# print(zetra1)

# helm1 = re.match('note-\d+', 'note-112334rwedafferg233')
# print(helm1)

# supra1 = re.match('\d+NOTE-\d+', '1264note-1232dsfe342'.upper())
# print(supra1)

# stel1 = re.match('[dsg]', 'd143rdadffffffdfg2ee2r')
# print(stel1)

# hepto1 = re.match('vyy', 'gghdtydyy4w445wyyv'[::-1])
# print(hepto1)

# seltum1 = re.match('zyz|cba', 'zyzabcasffedwdxyzxabc'[::-1])
# print(seltum1)

################################################
# output1 = re.search('Apples', text)
# print(output1)

# output2 = re.findall('is', text)
# print(output2)


output3 = re.finditer('le', text)
print(output3)
for match in output3:
    print(match)
    
# pattern = re.compile('an')

# output4 = pattern.findall(text)
# print(output4)


# output5 = pattern.search(text)
# print(output5)

# output6 = re.sub(pattern, '&&', text)   # substituting or replacing pattern with && 
# print(output6)
# print(text)

# test = '''alpha is great and great is beta but the great khali is also very'''
# output7 = re.split('great', test)
# print(output7)


# output8 = re.fullmatch('great', 'great')
# print(output8)