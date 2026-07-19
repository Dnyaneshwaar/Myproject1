# match statements

day=int(input("Enter the day: "))

match day:
    case 1:print("Sunday")
    case 2:print("Monday")
    case 3:print("Tuesday")
    case 4:print("Wednesday")
    case 5:print("Thursday")
    case 6:print("Friday")
    case 7:print("Saturday")
    case _:print("Invalid input")


# match statement with combine example

my_day= int(input("Enter the My day: "))
match my_day:
    case 2|3|4|5|6:print("weekday")
    case 1|7:print("Weekend day")
    case _:print("Invalid week")

# Example3

text_day= "sunday"

match text_day:
    case "monday"|"tuesday"|"wednesday"|"thursday" :print("weekday")
    case "sunday"|"sturday" :print("Weekend day")
    case _: print("Invalid week")





