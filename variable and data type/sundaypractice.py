# str1 = "Bhavya is my brother"
# print(str1.lower())
# print(str1.upper())
# # string1.capitalize() — Capitalizes the first character of the string.

# print(str1.capitalize())

# # string1.title() — Capitalizes the first character of each word.
# print(str1.title())
# # string1.swapcase() 
# print(str1.swapcase())
# str2 = "Bhavya is my brother and sunny is also my brother"
# # string1.find(substring) — Returns the index of the first occurrence of the substring, or -1 if not found.
# print(str2.find("my"))
# print(str2.find("oth"))

# string1.rfind(substring) — Returns the index of the last occurrence of the substring, or -1 if not found.
# print(str2.rfind("brother"))
# print(str2.rfind("rohan")) # if element is not in string then python always resturn -1

# # string1.index(substring) — Similar to find(), but raises a ValueError if the substring is not found.
# print(str2.index("brother"))
# print(str2.index("rohit"))  #throws an error :- value error

# string1.rindex(substring) — Similar to rfind(), but raises a ValueError if the substring is not found.
# print(str2.rindex("sunny"))
# print(str2.rindex("ashu"))  # throws a value error

# string1.replace(old, new) — Replaces all occurrences of a substring with another substri
# print(str2.replace('Bhavya is my brother and sunny is also my brother','nnoisd'))
# print(str2.rindex("n"))

#####################################################################################################

# str3 = ' she has 2040 rupees in her pocket '
# str4 = 'bckbaboifwbifrbwfibrfrfbfr'
# str5 = '723389479797439747'
# str6 = 'hwefwiohfre723447437'
# str7 = '                         '

# string2.startswith(substring) — Checks if the string starts with the specified substring.

# print(str3.startswith('hii'))  # false
# print(str3.startswith( ' she')) # true

# # string2.endswith(substring) — Checks if the string ends with the specified substring.
# print(str3.endswith('rohan')) #false
# print(str3.endswith('pocket '))  #true

# string2.isalpha() — Returns True if all characters are alphabetic.
# print(str3.isalpha()) #return false
# print(str4.isalpha()) #return true

# # string2.isdigit() — Returns True if all characters are digits.
# print(str3.isdigit())  #false
# print(str5.isdigit()) #true

# string2.isalnum() — Returns True if all characters are alphanumeric (letters and numbers).
# print(str3.isalnum()) # returns false
# print(str6.isalnum()) #returns true

# string2.isspace() — Returns True if all characters are whitespace.
# print(str3.isspace()) #false
# print(str7.isspace()) #True


# string2.islower() — Returns True if all characters are lowercase.
# print(str3.islower())  #true.
# print(str3.isupper())  #false.


# string2.isupper() — Returns True if all characters are uppercase.
# print(str3.isupper()) #false
# print(str3.upper())
# print (str3.replace(' she has 2040 rupees in her pocket ','HEY EVERYONE I AM SAURABH'))
# print(str3.islower())


# string2.istitle() — Returns True if the string is title-cased (each word starts with an uppercase letter).
# print(str3.istitle())
# str8  = '   She Has 2040 Rupees In Her Pocket   '
# print(str8.istitle())

#################################################################################33
#string2.strip() — Removes leading and trailing whitespace.
# print(str8.strip())
# print(str8)



#string2.lstrip() — Removes leading whitespace.
# print(str8.lstrip())


# #string2.rstrip() — Removes trailing whitespace.
# print(str8.rstrip())


################################################################################################################################################
# r = range(5)

# # Convert to a list
# print(list(r))  # Output: [0, 1, 2, 3, 4]

# # Convert to a tuple
# print(tuple(r))  # Output: (0, 1, 2, 3, 4)

# # Convert to a set
# print(set(r))    # Output: {0, 1, 2, 3, 4}

# tuple_students = (0,1,2,3,4,5,6,7)
# print(list(tuple_students))
# print(set(tuple_students))

##############################################################################################


######################        DICTIONARY          #####################################
# my_dict = dict({"name": "kumar", "age": 27, "city": "Hyderabad"})
# print(my_dict)
# print(type(my_dict))

# #####################################################################################
# my_dict1 = {"school": "st Xaviers school", "degree": "Graduations"}
# print(my_dict1)
# print(type(my_dict1))

# ##############################################################################
# my_dic = dict(one=1, two=2, three=3, four=4)
# print(my_dic)
# print(type(my_dic))
# ##############################################################################
# keys = ["name", "age", "city"]
# values = ["kumar", 27, "Hyderabad"]
# my_dict2 = dict(zip(keys, values))
# print(my_dict2)
# print(type(my_dict2))
# #################################################################################
# keys = ["name", "age", "city"]
# my_dict3 = dict.fromkeys(keys, "unknown")  # Sets all values to "unknown"
# print(my_dict3)
# print(type(my_dict3))
# ###################################################################################
# my_dict5 = dict([("name", "kumar"), ("age", 27), ("city", "Hyderabad")])
# print(my_dict5)
# print(type(my_dict5))

##########################################################################################3
# set1 = {637,737,87,737,837,73,837,9238}

# Adding:-
# my_set.add(6)
# set1.add(85)
# print(set1)

# Removing:-
# my_set.remove(5)   # Raises KeyError if element not found
# set1.remove(6)  # show error
# print(set1)
# my_set.discard(2)  # Does not raise error if element not found
# set1.discard(837)
# print(set1)
# clearing:-
# my_set.clear()     # Clears the whole set {Deletes the all elements of set.}
# set1.clear()
# set1.update([7, 8, 9])
# set1.update({10,23, 34})
# set1.update((1000, 2000, 3000))
# print(set1)
# set1.update(34, 56, 67)
# set1.pop()
# print(set1)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
	
# Union:-
# Returns a new set with elements from both sets.

# union_set = set1 | set2  
# print(union_set)
# Intersection:-
# Returns a new set with elements common to both sets.

# intersection_set = set1 & set2  # {3}
# print(intersection_set)

# Difference:-
# Returns a new set with elements in the set that are not in the other set.

# difference_set1 = set1 - set2  # {1, 2}
# difference_set2 = set2 - set1  # {4, 5}
# print(difference_set1)
# print(difference_set2)


# # Symmetric Difference:-
# # Returns a new set with elements in either set but not in both.

# sym_diff_set = set1 ^ set2  # {1, 2, 4, 5}
# print(sym_diff_set)
# set1 = {11, 22, 33, 44,100}
# set2 = {99, 33, 10, 200,100}

# # disjoint:-
# # Return True if two sets have a null intersection.

# print(set1.isdisjoint(set2) )  # False
# set1 = {76,27,28,29,30,34,35}
# set2 = {75,27,28,28,30,34,35}
# # print(len(set2))

# 	# difference_update:-
# 	# 	Remove all elements of another set from this set.
# 	# 	* set1.difference_update(set2)  # Removes all common elements from set1 which are 		  				  present in set2.
# set1.difference_update(set2)
# print(set1)
# set2.difference_update(set1)
# print(set2)

	# intersection_update:-
	# 	Update a set with the intersection of itself and another.
	# 	*set1.intersection_update(set2) # from set1 removes all elements which are not 							  present in set2.

	
	# issbuset:-
	# 	set3 = {1, 2, 3, 4}
	# 	set4 = {2, 3}
	# 	Report whether another set contains this set.
	# 	*set4.issubset(set3)   # if all the values of set4 are present in set3 it will 						 return True else false.


	# issuperset:-
	# 	set5 = {1, 2, 3, 4, 5}
	# 	set6 = {2, 3}
	# 	Report whether this set contains another set.
	# 	*set3.issuperset(set4)  # if set4 all elements are present in set5 it will return 					  True else false.


	# symmetric_difference:-
	# 	set1 = {100, 200, 300, 33, 44, 55}
	# 	set2 = {100, 200, 300, 33, 1000, 2000}
	# 	Return the symmetric difference of two sets as a new set.
	# 	*set3 = set1.symmetric_difference(set2) #It will create a new set called set3 								 which will have all non-common elements 							 from both the sets [set1 and set2]


	# symmetric_difference_update:-
	# 	set1 = {100, 200, 300, 33, 44, 55}
	# 	set2 = {100, 200, 300, 33, 1000, 2000}
	# 	Update a set with the symmetric difference of itself and another.
	# 	set1.symmetric_difference_update(set2)
	# 	print(set1)  # set1 will be updated with all non-common elements from set1 and 				       set2  


########################################################PRACTICE WITH CHATGPT######################

# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A|B)
# print(B.intersection(A))
# print(A.difference(B))
# print(B.difference(A))
# print(A.symmetric_difference(B))

# write a program to check if two sets are disjoint:
# set1 ={10,20,30}
# set2 = {40,50,60}
# set3 ={30,40,50}
# print(set1.isdisjoint(set2))
# print(set2.isdisjoint(set3))

# x = {1,2,3}
# y = {2,3,4}
# # x.difference_update(y)
# # print(x)
# # y.difference_update(x)
# # print(y)
# print(y.difference(x))
# p = {1,2,3,4}
# q = {3,4,5,6}
# r = {5,6,7,8}
# print(p.intersection(q))

# Math = {"Alice", "Bob", "Charlie", "David"}
# Science = {"Bob", "Charlie","Eve","Frank"}
# difference = Math-Science
# print(difference)
# difference1 = Science-Math
# print(difference1)
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# # print("addition",num1+num2)
# # print("substraction",num1-num2)
# # print("multiplication",num1*num2)
# # print("division",num1/num2)
# print("exponentiate",num1**num2)
# print("modulus",num1%num2)
# Comparison Operators Practice
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# Greater or lesser
# if num1 > num2:
# print(f"{num1} is greater than {num2}")
# elif num1 < num2:
# print(f"{num1} is less than {num2}")

# else:
# print("Both numbers are equal")
# print(15 & 13)
# print(bin(15))
# print(bin(23))
# print(bin(7))
# print(100|50)
# print(bin(100))
# print(bin(50))
# print(bin(10))
# print(bin(12))
# print(10^12)
# print(bin(6))
# print(bin(45))
# print(bin(32))
# print(45^32)
# print(bin6(13)) 
# print(10>>1)
# print(bin(5))
# print(bin(12))
# print(23>>2)
# print(bin(5))
# print(~10)
# print((bin(-11)))

# binary_num = "11110101"  
# integer_num = int(binary_num, 2)
# print(integer_num)
