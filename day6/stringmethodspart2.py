
# Splitting the strings - split()

s="abc@gmail.com"
lst = s.split("@")
print(lst)
print(lst[0])
print(lst[1])

t= "one,two,three"
lst1=t.split(",")
print(lst1)
print(lst1[2])

p= "User successfully created"
lst2 = p.split(" ")
print(lst2)

# trimming spaces - strip(),lstrip(),rstrip

s= "  hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(len(s))
