from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Window")
root.geometry("320x200")

Label(root, text="Please Login", font=("Arial", 14, "bold")).pack(pady=10)

Label(root, text="Username:").pack(anchor=W, padx=20)
entry_user = Entry(root, width=30)
entry_user.pack(padx=20, pady=5)

Label(root, text="Password:").pack(anchor=W, padx=20)
entry_pass = Entry(root, width=30, show="*")
entry_pass.pack(padx=20, pady=5)

# Inline check using lambda (simple for lab). Change "admin" and "1234" as needed.
Button(root, text="Login", width=12,
       command=lambda: (messagebox.showinfo("Login", "Login Successful")
                        if entry_user.get()=="admin" and entry_pass.get()=="1234"
                        else messagebox.showerror("Login", "Invalid username or password"))
).pack(pady=12)

root.mainloop()
