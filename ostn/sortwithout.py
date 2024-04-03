def bubble_sort(numbers):
    n = len(numbers)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# List of numbers
numbers = [5, 2, 9, 1, 7]

# Sort the numbers using bubble sort
bubble_sort(numbers)

print("Sorted list:", numbers)
