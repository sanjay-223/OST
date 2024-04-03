def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a

# Get input for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the HCF/GCD
hcf = gcd(num1, num2)
print(f"The HCF/GCD of {num1} and {num2} is {hcf}.")
