# set1 = {56,37,87,63,73}
# print(set1)
# print(type(set1))

# #adding
# set1.add(76)
# print(set1)
# #remove     ( Raises KeyError if element not found)
# set1.remove(87)
# print(set1)

# #discard (Does not raise error if element not found)
# set1.discard(63)
# print(set1)

# Updating Sets with Multiple Elements:
# set1.update([7, 8, 9])
# set1.update({10,23, 34})
# set1.update((1000, 2000, 3000))
# set1.update([34, 56, 67])
# print(set1)

# In Python, an arbitrary element is a random element.

# element = set1.pop()
# print(set1)
# Union:-
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# #Returns a new set with elements from both sets.
# union_set = set1 | set2  # {1, 2, 3, 4, 5}
# print(union_set)

# Difference:-
# Returns a new set with elements in the set that are not in the other set.

# difference_set1 = set1 - set2  # {1, 2}
# difference_set2 = set2 - set1  # {4, 5}
# print(difference_set1)
# print(difference_set2)

# Symmetric Difference:-
# Returns a new set with elements in either set but not in both.
# sym_diff_set = set1 ^ set2 
# print(sym_diff_set)
# set1 = {11, 22, 33, 44}
# set2 = {99, 33, 10, 200}

# disjoint:-
# Return True if two sets have a null intersection.
# set1.isdisjoint(set2)   # False
# print(set1)
# difference_update:-
# Remove all elements of another set from this set.
# set1.difference_update(set2)  # Removes all common elements from set1 which are 		  				  present in set2.
# print(set1)
# set2.difference_update(set1)
# print(set2)
# intersection_update:-
# Update a set with the intersection of itself and another.
# set1.intersection_update(set2)# from set1 removes all elements which are not 							  present in set2.
# print(set1)
# set2.intersection_update(set1)
# print(set2)
# issbuset:-
# set3 = {1, 2, 3, 4}
# set4 = {2, 3}
# Report whether another set contains this set.
# set4.issubset(set3)   # if all the values of set4 are present in set3 it will
set5 = {1, 2, 3, 4, 5}
set6 = {2, 3}
# Report whether this set contains another set.
set6.issuperset(set5)  # if set6 all elements are present in set5 it will return 					  True else false.
print(set5)

