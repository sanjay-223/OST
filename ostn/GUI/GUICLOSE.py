import tkinter as tk
def close_window(root):
    root.destroy()
def main():
    root = tk.Tk()
    root.title("Hello, World!")
    label = tk.Label(root, text="Hello, World!")
    label.pack()
    close_button = tk.Button(root, text="Close", command=lambda: close_window(root))
    close_button.pack()
    root.mainloop()
if __name__ == "__main__":
    main()