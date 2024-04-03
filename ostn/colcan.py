def vertical_concatenation(matrix):
    """Perform vertical concatenation of string variables in a 3x3 matrix."""
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
    concatenated_rows = ["".join(row) for row in transposed_matrix]
    return concatenated_rows

# Example usage
matrix = [
    ['apple', 'cat', 'red'],
    ['orange', 'dog', 'green'],
    ['banana', 'fish', 'blue']
]

concatenated_result = vertical_concatenation(matrix)
print("Vertical Concatenated matrix:")
for row in concatenated_result:
    print(row)
