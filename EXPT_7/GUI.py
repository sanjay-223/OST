import tkinter as tk
from tkinter import filedialog

def create_file():
    # Open a new file dialog
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write("This is a new file.")

def save_file():
    # Open a file dialog to save an existing file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        with open(file_path, 'w') as file:
            # Write some content to the file (for demonstration)
            file.write("This is the content of the saved file.")

def print_file():
    # Open a file dialog to select a file to print
    file_path = filedialog.askopenfilename(filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        # For demonstration, just print the file path to the console
        print("Printing file:", file_path)

root = tk.Tk()
root.title("File Operations Example")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Print", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()