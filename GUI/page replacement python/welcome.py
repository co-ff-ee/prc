from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Welcome Screen")
root.geometry("300x200")

Label(root, text="Welcome to Python GUI", font=("Arial", 14)).pack(pady=15)

Label(root, text="Enter your name:").pack()
e_name = Entry(root)
e_name.pack(pady=5)

Button(root, text="Continue", width=10,
       command=lambda: messagebox.showinfo("Hello", "Welcome " + (e_name.get() or "User") + "!")
).pack(pady=5)

Button(root, text="Exit", width=10, command=root.destroy).pack(pady=5)

root.mainloop()
