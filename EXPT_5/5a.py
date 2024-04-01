age = int(input("Enter the age: "))

try:
    if age<18:
        raise ValueError("You must be at least 18 years old")
    elif age>100:
        raise ValueError("Invalid age. Above 100")
    print("You are eligible to vote")
except ValueError as v:
    print("Error: ",v)  