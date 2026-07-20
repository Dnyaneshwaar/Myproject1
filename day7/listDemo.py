# creating list
from itertools import count

# A list is a collection which is ordered and changeable.
# In Python lists are written with square brackets [ ].
# List is mutable.  

# my_list = ["10","Apple",True]
# print(my_list)
#
# my_list = []  # Empty list

# Access items/values/objects

my_list1 = ["apple","banana","cherry"]  #Index start from 0.

print(my_list1[0]) # apple
print(my_list1[2]) # cherry

print(my_list1[-1]) # cherry
print(my_list1[-2]) # banana


# Access multiple values form list (range of indexes)

my_list2 = ["apple","banana","cherry","orange","kiwi","melon","mango"]

print(my_list2[2:5]) # ['cherry', 'orange', 'kiwi']
print(my_list2[-4:-1]) # ['cherry', 'orange', 'kiwi', 'melon']

# Change the item value from list


my_list3 = ["apple","banana","cherry"]

print("Before the change", my_list3)
my_list3[0]="orange"
print("After the change", my_list3)

# loop with list - mostly for loop

my_list4 = ["apple","banana","cherry"]

for i in my_list4:
    print(i)

# check if the item is existed in list

my_list5 = ["apple","banana","cherry"]

if "banana" in my_list5:
    print("banana is present")
else:
    print("banana is not present")


# for i in my_list5:
#     if i=="banana":
#         print(f"Item {i} is present in list")

# find out length/size of list

my_list6 = ["apple","banana","cherry"]
print(len(my_list6))

# find count number of time repeated in list

my_list7= ["apple","banana","cherry","apple","apple"]

var= my_list7.count("apple")
print(var)

# Sorting list - By default Ascending order

my_list8 = ["cherry","mango","banana","apple"]

print("Before sort: ",my_list8)
my_list8.sort()                        # sort element in Ascending order
print("After sort: ",my_list8)
my_list8.sort(reverse=True)              # sort element in Descending order
print("After sort in descending order: ",my_list8)

# Revers the List
# pre-requisite- values must be in sorted order

my_list9 = ["mango","banana","cherry","apple"]

print("Before reverse: ",my_list9)
my_list9.sort()
print("After sort: ",my_list9)
my_list9.reverse()
print("After reverse: ",my_list9)

# append the list

list1 = ["apple","banana","cherry"]
list2= ["10","20","30"]

for i in list2:
    list1.append(i)
print("append list2 using loop: ", list1)

# append the list using extend()

list3 = ["apple","banana","cherry"]
list4= ["10","20","30"]

list3.extend(list4)
print(list3)
