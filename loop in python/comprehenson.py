# # List Comprehension:-

# # 1) Create a list which has 0 to 10 numbers:-
# # 0,1, 2, 3, 4, 5, 6, 7, 8, 9

# list_of_nums = [0,1, 2, 3, 4, 5, 6, 7, 8, 9] # ----> statically entering data into list.
# print(list_of_nums)

# # ----------------------------------------------------------------

# list_of_nums1 = []

# for i in range(10):
#     list_of_nums1.append(i)
    
# print(list_of_nums1)

# # ---------------------------------------------------------------------

# list_of_nums2 = [i for i in range(10)]
# print(list_of_nums2)


# #----------------------------------------------------------------------

# squares_of_nums = [i ** 2 for i in range(10)]
# print(squares_of_nums)

# cubes_of_nums = [i**3 for i in range(10)]
# print(cubes_of_nums)

# double_of_nums = [i+i for i in range(10)]
# print(double_of_nums)

# half_of_nums = [i/2 for i in range(10)]
# print(half_of_nums)

# mod_of_nums = [i % 2 for i in range(10)]
# print(mod_of_nums)

# # from 0 to 20 print only even numbers.

# even_nums = [i for i in range(20) if i % 2 == 0]
# print(even_nums)

# odd_nums = [i for i in range(20) if i % 2 != 0]
# print(odd_nums)

# div_by_3 = [i for i in range(30) if i % 3 == 0]
# print(div_by_3)


# div_by_5 = [i for i in range(17, 55) if i % 5 == 0]
# print(div_by_5)

# # range 13, 65 find the numbers which are divisible by 7 and do the square of it.

# square_of_num_div_by_7 = [i ** 2 for i in range(13, 65) if i % 7 == 0]
# print(square_of_num_div_by_7)


# #-------------------------------------------------------------------

# months_in_small = ['january', 'february', 'march', 'april', 'may'] 

# months_in_upper = [i.upper() for i in months_in_small]
# print(months_in_upper)

# rev_of_months = [i[::-1] for i in months_in_small]
# print(rev_of_months)

# str1 = '8i76j567l876f54j3hr3423i456'

# chhar_of_list = [i for i in str1 if i.isalpha()]
# print(chhar_of_list)

# nested_list = [[[100, 200], [300, 400]], [[500, 600], [700, 800]], [[900, 1000], [1100, 1200]]]   # [1, 2, 3, 4, 5, 6]

# for i in nested_list:
#     for j in i:
#         for k in j:
#             print(k)
        
# nested_list = [[1, 2], [3, 4], [5, 6]]
# flattened = [item for sublist in nested_list for item in sublist]
# print(flattened)

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# for x in list1:
#     for y in list2:
#         print((x, y))

# cartesian_product = [(x, y) for x in list1 for y in list2]
# print(cartesian_product)



# tuple comprehensions

# tup1 = (i for i in range(10))
# print(tup1)   #<generator object <genexpr> at 0x000001E81DC4C0B0>

# for i in tup1:
#     print(i)
    
    
    
# dictionary comprehensions...

# dict1 = {i: i**3 for i in range(10)}
# print(dict1)
# print(type(dict1))


# dict2 = {i: i **2 for i in range(20) if i % 2 ==0}
# print(dict2)


# dict3 = {i: i **2 for i in range(100) if i % 3 ==0 and i % 5 ==0}
# print(dict3)



# dict4 = {1: 1, 2: 4, 3: 9, 4: 16, 5:25, 6:36, 7:49, 8: 64, 9: 81, 10: 100, 11: 121, 12:144, 15: 225, 16: 256, 17: 289}

# dict5 = { key: value for key, value in dict4.items() if value % 2 == 0}
# print(dict5)

# dict6 = {value: key for key, value in dict4.items()}
# print(dict6)


# dict7 = {i: ('even' if i % 2 == 0 else 'odd') for i in range(20)}
# print(dict7)


# list_str = ['APPLE','apple', 'Apple', 'aPPlE']


# unique_squares = [x**2 for x in range(-5, 6)]

# print(unique_squares)
# str1 = 'Alpenlibejilulchaye'
# vowel= 'aeiouAEIOU'
# new_str = {i : ('vowel' if i.upper() in str1 else 'consonent') for i in str1 }
# print(new_str)
# list_of_keys=['Apple','orange','pineapple','banana','grapes']
# list_of_values = ['vit-D','vit-C','vit-G','vit-x','vit-p']
# dict5 = {keys:values for keys,values in zip(list_of_keys,list_of_values)}
# print(dict5)