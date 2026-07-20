
# Function with arbitrary arguments

def sum_function(*numbers):
    total=0
    for i in numbers:
        total=total+i
    return total

print(sum_function(1,2,3,4,5,6))
print(sum_function(10,20,30,40,50,60))