# create /write file

# with open("C:\\Users\\Dnyaneshwaar\\PycharmProjects\\automation Files\\myfile.txt",'w') as file:
#     file.write("Welcome to file")
#     file.close()

# Append the data

# with open("C:\\Users\\Dnyaneshwaar\\PycharmProjects\\automation Files\\myfile.txt",'a') as file:
#     file.write(" \n This is appending data call")
#     file.close()

# read()- read all the content from file
# readline() -   read the single line
# readlines()- read all the lines into list format.

# with open("C:\\Users\\Dnyaneshwaar\\PycharmProjects\\automation Files\\myfile.txt",'r') as file:
#     file_Content = file.readlines()
#     print(file_Content)

# Delete the file

import os

file = "C:\\Users\\Dnyaneshwaar\\PycharmProjects\\automation Files\\myfile.txt"

if os.path.exists(file):
    os.remove(file)
else:
    print("file not exist")

# get Current folder
import os
print(os.getcwd())


