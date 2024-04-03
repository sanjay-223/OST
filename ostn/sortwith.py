# List of numbers
numbers = [5, 2, 9, 1, 7]

# Sort the numbers using sort method
numbers.sort()

print("Sorted list:", numbers)
# Sort in descending order using sorted function
sorted_numbers_desc = sorted(numbers, reverse=True)

# Sort in descending order using sort method
numbers.sort(reverse=True)

print("Sorted list in descending order (sorted function):", sorted_numbers_desc)
print("Sorted list in descending order (sort method):", numbers)
