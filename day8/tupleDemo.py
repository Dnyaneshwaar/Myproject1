# Creating tuple

# my_tuple = ("apple","banana","cherry")
#
# print(my_tuple)
#
# #accessing values/elements
#
# print(my_tuple[0])
# print(my_tuple[1])

# range of indexes

# my_tuple = ("apple","banana","cherry","orange","kiwi","mango")
#
# print(my_tuple[2:5])
# print(my_tuple[-4:-2])

# change the value of tuple "Indirect way"
# tuple-->list--->tuple

# my_tuple = ("apple","banana","cherry")
#
# my_list = list(my_tuple)
# print("After tuple modify to list", my_list)
# my_list[1]="orange"
# print("After changing list value: ",my_list)
# my_tuple=tuple(my_list)
# print("After changing list to tuple: ", my_tuple)

# item exist or not

# my_tuple = ("apple","banana","cherry")
#
# if "cherry" in my_tuple:
#     print("It is present")
# else:
#     print("It is not present")

# count the items

# my_tuple = ("apple","banana","cherry")
#
# print(len(my_tuple))

# adding & removes values is not allowed in tuple as it's immutable

# copying the tuples

# my_tuple1 = ("apple","banana","cherry")
# my_tuple2 = my_tuple1
# print(my_tuple2)

# joining the tuples

my_tuple1 = ("apple","banana","cherry")
my_tuple2 = (10,20,30)

my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)

