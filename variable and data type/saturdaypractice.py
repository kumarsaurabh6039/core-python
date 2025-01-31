# dictionary, frozenset, range, string buit in methods -----> Surabh

# set, frozenset, range ----> Sahil

# set, frozenset, range -----> Pavani

# reference, shall, deep copy  ------> samir

# set, frozenset, range  -----> shabista

# dictionary, set, frozenset, range, byte and bytearray -----> rahul

# Frozenset, range, bytearray  ----> konda


# string, dictionary, set, frozenset, range, byte, bytearray, reference, shallow copy, deep copy ----> shivkumar



# string:- 
# str1 = 'python is easy @ sabik'
# str2 = 'MUMBAI is Great City'

# lower
# print(str1.lower())
# print(str2.lower())


# upper
# print(str1.upper())
# print(str2.upper())


# capitalize
# print(str1.capitalize())
# print(str2.capitalize())



# title
# print(str1.title())
# print(str2.title())

# swapcase
# print(str1.swapcase())
# print(str2.swapcase())


# search and replace
# str3 = 'America is the big nation, It is a diverse country open to all corners of the wolds people. the populaton of US is 3 billion, open country'


# find

# print(str3.find('corners'))
# print(str3.find('color'))  # returns -1
# rfind
# where string ends that side is called right side of string.
# where string starts that side is called left side of string.
# print(str3.rfind('the'))
# print(str3.rfind('Jamun'))   # return -1

# index
# print(str3.index('billion'))
# print(str3.index('hyderabd'))  # throws an error ;- valueError

# # rindex
# print(str3.rindex('open'))
# print(str3.rindex('the'))
# print(str3.rindex('rohit'))   # throws an error ;- vaueError

# replace

# print(str3.replace('country', 'Nation'))

# print(str3)


# temperory and permanent change

# str1 = 'Wankhed Stadium'

# print(str1.lower())  # temperory
# print(str1)   


# str1 = ' I have 2345 Rs in my pocket   '

# # startswith
# print(str1.startswith('hello'))
# print(str1.startswith('I'))
# print(str1.startswith(' '))
# print(str1.startswith(' I'))
# print(str1.startswith(' I hav'))


#endswith

# print(str1.endswith('baboon'))
# print(str1.endswith('pocket'))
# print(str1.endswith('pocket '))
# print(str1.endswith('cket   '))


# str1 = ' I have 2345 Rs in my pocket   '

# str2 = '34567.56'

# str3 = '3456sdfgh'

# print(str1.isalnum())
# print(str3.isalnum())
# print(str2.isalnum())

# print(str1.isdigit())
# print(str2.isdigit())

# str2 = 'jhcgfhfgj'
# print(str1.isalpha())
# print(str2.isalpha())


# str1 = '   .'
# print(str1.isspace())

# str2 = 'fghjuygf %vbh g'
# print(str2.islower())

# str3 = 'FHGHJBNHFG  #HNNMN t'

# print(str3.isupper())


# str1 = 'Python Language Is Great.'
# print(str1.istitle())


# str2 = '   Indian Economy is booming.  '
# print(str2)

# print(str2.strip())

# print(str2.lstrip())
# print(str2.rstrip())

########################################################################################

# dictionary

# colors = {'Blue': 'Peace', 'green': 'life', 'white': 'jesus', 'safron': 'hindu', 'black': 'devil', 'yellow': 'Australia'}
# print(colors)
# print(type(colors))

# print()

# games = dict({'game1': 'cricket', 'game2': 'hockey', 'game3': 'kabaddi', 'game4': 'football'})
# print(games)
# print(type(games))

# print()

# food = dict(One=1, Two=2, Three=3, kondu='kabaddi', sohail='dataAnalytics', diesel=True)
# print(food)
# print(type(food))


# print()

# list_of_keys = ['Veg Biryani', 'Nan', 'Dal', 'Mitthi Dal', 'Paneer']

# list_of_values = ['Mandi', 'Shwarma', 'khubsa', 'falafil', 'haleem']

# veg_non_veg = dict(zip(list_of_keys, list_of_values))

# print(veg_non_veg)

# list_keys = [123, 345, 677, 999, 4567]

# num_type = dict.fromkeys(list_keys, 'odd')
# print(num_type)
# print(type(num_type))


# dict_tup = dict([('name', 'sohail'), ('age', 24), ('school', 'st Xavier')])
# print(dict_tup)
# print(type(dict_tup))

# Accessing elements

# dict1 = {'color': 'Pink', 'food': 'Biryani', 'boy': 'Rahul', 'girl': 'Shabista', 'age': 45}

# dict_keys = dict1.keys()
# print(dict_keys)
# print(type(dict_keys))

# print('--------------------------------------------------------------------------------------')

# list_keys = list(dict_keys)
# print(list_keys)
# print(type(list_keys))

# print('----------------------------------------------------------------------------------')

# dict_values =  dict1.values()
# print(dict_values)
# print(type(dict_values))

# print('-----------------------------------------------------------------------------------')

# list_values = list(dict_values)
# print(list_values)
# print(type(list_values))

# print('--------------------------------------------------------------------------------------')

# print(dict1['color'])
# print(dict1['age'])
# print(dict1['food'])
# print(dict1['boy'])

# print('--------------------------------------------------------------------------------------')

# print(dict1.get('boy'))
# print(dict1.get('food'))
# print(dict1.get('color'))


# print('---------------------------------------------------------------------------------------')


# dict2 = {'subject': 'Python', 'class': 'seventh', 'language': 'Hindi', 'Tv':  'Bravia', 'ronaldo': 'football'}

# dict2['Movie'] = 'Pushpa 2'

# dict2['subject'] = 'Java'


# print(dict2.pop('ronaldo'))
# print(dict2.pop('man'))

# del dict2['language']

# dict2.popitem()

# dict2.clear()


# print(dict2)

# dict_items = dict2.items()
# print(dict_items)
# print(type(dict_items))

# dict_small = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
# dict2.update(dict_small)


# dict2.setdefault('River')

# dict2['River'] = 'Narmada'

# print(dict2)


# dict1 = {'Person': {'name': 'Rohit', 'age': 23, 'City': 'Karnool', 'Salary': 56000}, 'Horse': {'Owner': 'Sameer', 'breed': 'Arabian', 'height': 6, 'weight': 200}}
# print(dict1['Person']['City'])


# dict1['Horse']['breed'] = 'Kathiyawadi'
# print(dict1['Horse']['breed'])


#################################################################################################

# print(range(5))  # 0, 1, 2, 3, 4

# print(range(4, 10))   # 4, 5, 6, 7, 8, 9

# print(range(5, 15, 2))  # 5, 7, 9, 11, 13


# range1 = range(4, 15, 3)  # 4, 7, 10, 13

# print(max(range1))
# print(min(range1))

# print(len(range1))

# print(range1.count(4))
# print(range1.count(14))

# print(range1[0])
# print(range1[3])
# print(range1[-1])
# print(range1[-1:-5: -1])
# print(range1[11: 3: -1])


# range_alpha = range(2, 23, 2)

# print(range_alpha)
# print(type(range_alpha))
# print('--------------------------------------------------------------------------------------')

# list_alpha = list(range_alpha)
# print(list_alpha)
# print(type(list_alpha))

# print('-----------------------------------------------------------------------------------------')

# tup_alpha = tuple(range_alpha)
# print(tup_alpha)
# print(type(tup_alpha))


# print('--------------------------------------------------------------------------------------')

# set_alpha = set(range_alpha)
# print(set_alpha)
# print(type(set_alpha))

###############################################################################################

# set1 = set()
# print(set1)
# print(type(set1))

# set2 = {12}
# print(set2)
# print(type(set2))

# set3 = {12, 24, 36, 48, 60 ,72}

# print(22 in set3)

# Add element to set3

# set3.add(84)
# print(set3)

# Remove the element from set

# set3.remove(12)
# print(set3)
# # set3.remove(25)


# set3.discard(60)
# print(set3)
# set3.discard(25)

# set3.pop()

# set3.clear()
# print(set3)


# set3.update(['A', 'B', 'C'])
# set3.update(('a', 'b', 'c'))
# set3.update({1, 2, 3, 4})
# # set3.update(78, 88, 89, 90)    # error
# print(set3)




set1 = {1, 2, 3, 5}
set2 = {3, 5, 8, 9, 11}

# Union

# set3 = set1 | set2
# print('Union: ',set3)

# Intersection

# set4 = set1 & set2
# print('Intersection: ',set4)


# difference
# set5 = set1 - set2
# print('difference: ',set5)

# set6 = set2 - set1
# print('Difference: ',set6)


# Symmetric Difference

# set7 = set1 ^ set2
# print('Symmetric Difference: ',set7)

# print('-----------------------------------------------------------------------------------------')


# print(set1.isdisjoint(set2))

# set1.difference_update(set2)
# set2.difference_update(set1)
# set1.intersection_update(set2)
# set2.intersection_update(set1)


# print(set1)
# print(set2)


# set100 = {1, 2, 3}
# set200 = {8, 9, 7,6}

# print(set100.isdisjoint(set200))



set1 = {12, 34, 56, True, 100, 0, False}
set2 = {0, 1, 56, 'A', "Z", 67}

# print(set1.issuperset(set2))
# print(set2.issubset(set1))

# set3 = set1.symmetric_difference(set2)
# set1.symmetric_difference_update(set2)

# print(set1)
# print(set2)
# print(set3)


###################################################################################################

# f_s1 = frozenset({1, 2, 3, 4, 3})
# print(f_s1)
# print(type(f_s1))

# f_s2 = frozenset('Hello')
# print(f_s2)
# print(type(f_s2))

# f_s3 = frozenset(['A', 'B', 'C', 'D'])
# print(f_s3)
# print(type(f_s3))


# f_s4 = frozenset(('z', 'x', 'c', 'v'))
# print(f_s4)
# print(type(f_s4))

# print('z' in f_s4)



# f1 = frozenset([1, 2, 3, 4])
# f2 = frozenset([3, 4, 5, 6, 7])

# f10 = f1.difference(f2)
# print(f10)

# f11 = f2.difference(f1)
# print(f11)

# f12 = f1.intersection(f2)
# print(f12)




#Union
# f3 = f1 | f2
# print(f3)
# print(type(f3))

# Difference

# f4 = f1 - f2
# print(f4)

# f5 = f2 -f1
# print(f5)


#symmetric difference

# f6 = f1 ^ f2
# print(f6)


#intersection
# f7 = f1 & f2
# print(f7)

# set99 = frozenset([100, 200, 300, 400])   # superset of set88
# set88 = frozenset([200, 300])   # subset of set99

# print(set88.issubset(set99))
# print(set99.issuperset(set88))

# print(set99.isdisjoint(set88))