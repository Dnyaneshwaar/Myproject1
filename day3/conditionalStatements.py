# Conditional statements in python- if, if-else, if-elif-else, match statement

# if
amount=1800
discount1=0

if amount>=1500:
    discount1=amount*10/100

print("Actual amount after discount", amount-discount1)

# If else
age= 21

if age>=18:
    print("eligible for vote")

else:
    print("Not eligible for vote")

# example2- check the amount value after the discount

# if elif else

total_amount = 11000

print("Actual amount:" , total_amount)

if total_amount >=10000:
    discount=total_amount*20/100
elif total_amount >=5000:
    discount=total_amount*10/100
elif total_amount >=2000:
    discount=total_amount*5/100
else:
    discount=0

print("Actual amount:", total_amount-discount)


#Nested if else

num=1

print("Actual number: ",num)

if num%2==0:
    if num%3==0:
        print("number divisible by 2 & 3")
    else:
        print("number divisible by 2 only")
else:
    if num%3==0:
        print("number divisible by 3 only")
    else:
        print("number is not by divisible 2 & 3")



