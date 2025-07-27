num = 10
if num >11:
    print("num is greater")
else:
    print("num is exceed")


a1 = 12
if a1 >= 10 and a1 <=20:
    print("a1 is in given range")
else:
    print("a1 is in not given range")


age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


marks = int(input("Enter your marks:"))
if marks >=90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("FAIL")



age = int(input("Enter your age: "))
nationality = input("Enter your Nationality: ")
if age >=18 and nationality == "indian":
    print("You can vote") 
else:
    print("You cannot vote")