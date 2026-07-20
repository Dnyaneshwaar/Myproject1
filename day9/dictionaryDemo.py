
# creating dictionary

#Approch1

# my_dict={"brand":"Ford","model":"Mustang","year":2007}
# print(my_dict)

#Approch2 - using dict() constructor

# my_dict=dict(name="John",Age=25)
# print(my_dict)

# Key can have multiple values

# my_dict={"brand":"Ford",
#          "model":"Mustang",
#          "year":2007,
#          "color":["red","green","blue"]
#          }
#
# print(my_dict)

# Access item from dictionary
#Approch-1 by key

# my_dict={"brand":"Ford","model":"Mustang","year":2007}
# print(my_dict["model"])

#Approch-2 using get method

# my_dict={"brand":"Ford","model":"Mustang","year":2007}
# print(my_dict.get("model"))

# looping dictionary

# my_dict={"brand":"Ford","model":"Mustang","year":2007}
# #print(my_dict.keys())
#
# for x in my_dict:
#     print(x)
#
# for x in my_dict.keys():
#     print(x)
#
# # print values only
# for x in my_dict.values():
#     print(x)
#
# for x in my_dict:
#     print(my_dict[x])

# print key,values

my_dict={"brand":"Ford","model":"Mustang","year":2007}

for x,y in my_dict.items():
    print(x,y)