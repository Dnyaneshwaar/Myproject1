
# String is immutable, Cannot be changed after creation

# Example1: - same variable but different memory location.

s1= "hello"

print(s1)
print(id(s1))

s1= "H"+s1[1:]
print(s1)
print(id(s1))

# Example2:

s1="python"

print("Before replace: ", id(s1))
print(s1)

s1=s1.replace("p","P")
print("After replace: ", id(s1))
print(s1)

# List- mutable object, can be changed after creation

myList = ["h","e","l","l","o"]
print("Original list", myList)
print("Original list", id(myList))

myList[0]="H"

print("After modification", myList)
print("After modification", id(myList))
