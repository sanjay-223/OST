def get_matrix(rows, cols):
    """Get a matrix from the user."""
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements for row {i+1} (separated by space): ").split()))
        if len(row) != cols:
            print("Error: Please enter the correct number of elements.")
            return None
        matrix.append(row)
    return matrix

def display_column(matrix, col_num):
    """Display the kth column of the matrix."""
    if col_num < 0 or col_num >= len(matrix[0]):
        print("Error: Column number out of range.")
        return
    column = [row[col_num] for row in matrix]
    print(f"Column {col_num+1}:", column)

# Get input for matrix dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get the matrix from the user
matrix = get_matrix(rows, cols)
if matrix is not None:
    # Get the column number to display
    k = int(input("Enter the column number to display (0-based indexing): "))
    display_column(matrix, k)
