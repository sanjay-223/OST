import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Hello, World!")
    label = tk.Label(root, text="Hello, World!")
    label.pack()
    root.mainloop()
if __name__ == "__main__":
    main()