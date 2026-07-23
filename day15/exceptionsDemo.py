# try:
#     print(x)
# except:
#     print("An exception occurred..")
# print("Finished")


# many exception
#
# try:
#     print(x)
#
# except NameError:
#     print("This is name error")
# except:
#     print("An exception occurred..")
# print("Finished")

# try, except, else & finally

try:
    n= int(input("enter a number: "))
    result= 100/n
except ZeroDivisionError:
    print("number can't be zero")
except ValueError:
    print("enter valid number")
else:
    print(result)
finally:
    print(" finally executed")
