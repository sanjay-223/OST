class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def display(self):
        print("Stack contents:", self.items[::-1])

# Example usage with user input
stack = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.push(item)
    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print("Popped item:", popped_item)
    elif choice == '3':
        stack.display()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
