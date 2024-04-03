def get_natural_number(prompt):
    """Get a natural number (positive integer excluding zero) from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Please enter a natural number (positive integer excluding zero).")
            elif value==0:
                raise ValueError("you have entered zero(please enter positive integer excluding zero).")
            return value
        except ValueError as e:
            print(e)

# Get input for the natural number
number = get_natural_number("Enter a number : ")
print(f"You entered the natural number: {number}")
