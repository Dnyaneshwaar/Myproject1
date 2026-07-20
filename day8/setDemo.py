#Set is unordered(item stored in random order), store all type of data
#index is not supported
#duplicates are not allowed
# set is mutable


# creating set

# my_set1= {"apple","banana","cherry"}
# my_set2= {10,20,30,40,50}
# my_set3= set()  # empty set
#
# print(my_set1)
# print(my_set2)

# Accessing the elements/item is not possible by index as set is not supported index

# can't change item in set, but we can add item in set.

# Access data from set using for loop
#
# my_set1 = {"apple","banana","cherry"}
#
# for i in my_set1:
#     print(i)

# searching value in set - using in operator

# my_set1 = {"apple","banana","cherry"}
#
# if "cherry" in my_set1:
#     print("It is present in the set")
# else :
#     print("It is not present in the set")

# length of set

# my_set1 = {"apple","banana","cherry"}
# print(len(my_set1))

# Sorting, Reverse is possible in set bcz data is not in order.s

# Add items in set

# my_set1 = {"apple","banana","cherry"}
#
# # my_set1.add("orange")
# # print("After adding item in set", my_set1)
#
# my_set1.update(["orange","mango"])
# print("After adding item in set", my_set1)

# if you have duplicate values in set it will ignore

# my_set2 = {1,1,2,3,2,4}
# print(my_set2)  # {1, 2, 3, 4}

# Remove element
#Approch1: using remove(), discard() - both are same.
# if value is not available in set remove() method give "KeyError" & discard() not giving error.

# my_set={"apple","banana","cherry"}
# my_set.remove("cherry")
# print(my_set)

# Approach2 - pop()- remove random element

# my_set={"apple","banana","cherry"}
# my_set.pop()
# print(my_set)

# Retrieving common values -
# Approach1- intersection()

my_set1= {"apple","banana","cherry",10}
my_set2={10,20,30,"apple"}

my_set3=my_set1.intersection(my_set2)
print(my_set3)

# Approach2- &

my_set1= {"apple","banana","cherry",10}
my_set2={10,20,30,"apple"}

my_set3=my_set1&my_set2
print(my_set3)