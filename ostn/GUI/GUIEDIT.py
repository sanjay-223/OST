import tkinter as tk
from tkinter import Menu
def do_nothing():
    pass
def main():
    root = tk.Tk()
    root.title("GUI with Dropdown Toolbar")
    menubar = Menu(root)
    root.config(menu=menubar)
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="New File", command=do_nothing)
    file_menu.add_command(label="Save", command=do_nothing)
    file_menu.add_command(label="Print", command=do_nothing)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    root.mainloop()
if __name__ == "__main__":
    main()