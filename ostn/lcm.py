def lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
print(f"The LCM of {num1} and {num2} is ",lcm(num1, num2))