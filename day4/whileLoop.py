
#
# two type of loops mainly used in python
# 1. While loop
# 2. For loop
#
# While loop executes as long as condition is true
#
# example1: print 1 to 10 numbers


i=1
while i<=10:
    print("Numbers: ",i)
    i=i+1

# example2: print even numbers
#method1
i=2
while i<=10:
    print("Even Numbers: ",i)
    i=i+2

#method1 - even number start with 1

i=1
while i<=10:
    if i%2==0:
        print("even numbers: ",i)
    i=i+1

#method2 - odd number start with 1

i=1
while i<=10:
    if i%2!=0:
        print("Odd number is: ",i)
    i=i+1

# print 1-10 numbers in descending order

i=10

while i>=1:
    print("Numbers in descending order: ",i)
    i=i-1





