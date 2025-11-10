from tkinter import *

root = Tk()
root.title("ERP System Prototype")
root.geometry("400x300")

Label(root, text="ERP System", font=("Arial", 16, "bold")).pack(pady=10)

# Login Section
Label(root, text="Username:").pack(anchor=W, padx=20)
e_user = Entry(root, width=30)
e_user.pack(padx=20)

Label(root, text="Password:").pack(anchor=W, padx=20)
e_pass = Entry(root, width=30, show="*")
e_pass.pack(padx=20, pady=5)

Button(root, text="Login", width=10).pack(pady=10)

# Dashboard section (as prototype only)
Label(root, text="Modules:", font=("Arial", 12, "bold")).pack(anchor=W, padx=20, pady=5)
Button(root, text="Student Info", width=15).pack(anchor=W, padx=40)
Button(root, text="Attendance", width=15).pack(anchor=W, padx=40)
Button(root, text="Fees", width=15).pack(anchor=W, padx=40)
Button(root, text="Exams", width=15).pack(anchor=W, padx=40)

root.mainloop()
