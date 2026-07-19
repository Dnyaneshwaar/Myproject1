
# range function- range(start,end,increment or decrement)
# range(n) - range(10)- starting point -0 & end point 'n-1' ==> 0,1,2,3,4,5,6,7,8,9
# range(a,b) -range(0,10) - starting point -a & end point 'b-1' ==> 0,1,2,3,4,5,6,7,8,9
# range(a,b,c) -range(2,10,2) - starting point -a & end point 'b-1' & increment by 2 ==> 2,4,6,8

# #Example1
# for i in range(1,11):
#     print(i)

#Example2- print even number
# Method-1
# for i in range(2,10,2):
#     print(i)

#Method-2

# for i in range(1,10):
#     if i%2==0:
#         print(i)

# Example-3 - print reverse number -10 to 1
for i in range(10,0,-1):
    print(i)


