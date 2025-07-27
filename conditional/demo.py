# Sample code with match-case  statement or elif ladder

age = int(input("Enter your age: "))
if age == 0 or age ==1 or age ==2 or age ==3 or age ==4:
    category = "Toddler"
elif age == 5 or age == 6 or age == 7 or age == 8 or age == 9:
    category = "Child"
elif age == 10 or age == 11 or age == 12 or age == 13 or age == 14:
    category = "Teenager"
else:
    category = "Adult"

    print(category)



    age = 15
    if age in (0,1,2,3,4):
        print("Toddler")
    elif age in (5,6,7,8,9):
        print("Child")
    elif age in (10,11,12,13,14):
        print("Teenager")
    else:
        print("Adult")
        