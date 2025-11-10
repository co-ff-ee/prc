from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Sign Up")
root.geometry("380x420")

Label(root, text="Create an Account", font=("Arial", 16, "bold")).pack(pady=10)

# Full Name
Label(root, text="Full Name:").pack(anchor=W, padx=20)
entry_name = Entry(root, width=35)
entry_name.pack(padx=20, pady=5)

# Username
Label(root, text="Username:").pack(anchor=W, padx=20)
entry_user = Entry(root, width=35)
entry_user.pack(padx=20, pady=5)

# Email
Label(root, text="Email:").pack(anchor=W, padx=20)
entry_email = Entry(root, width=35)
entry_email.pack(padx=20, pady=5)

# Password
Label(root, text="Password:").pack(anchor=W, padx=20)
entry_pass = Entry(root, width=35, show="*")
entry_pass.pack(padx=20, pady=5)

# Confirm Password
Label(root, text="Confirm Password:").pack(anchor=W, padx=20)
entry_cpass = Entry(root, width=35, show="*")
entry_cpass.pack(padx=20, pady=5)

# Phone (optional)
Label(root, text="Phone (optional):").pack(anchor=W, padx=20)
entry_phone = Entry(root, width=35)
entry_phone.pack(padx=20, pady=5)

# Agree to terms
agree = IntVar()
Checkbutton(root, text="I agree to the Terms and Conditions", variable=agree).pack(pady=10)

# Submit button - inline checks:
# 1) must agree to terms
# 2) passwords must match
# 3) username and email should not be empty (simple check)
Button(root, text="Sign Up", width=15,
       command=lambda: (
           messagebox.showerror("Error", "Please accept Terms and Conditions")
           if agree.get()==0 else
           (messagebox.showerror("Error", "Password and Confirm Password do not match")
            if entry_pass.get() != entry_cpass.get() else
            (messagebox.showerror("Error", "Username and Email cannot be empty")
             if entry_user.get().strip()=="" or entry_email.get().strip()=="" else
             messagebox.showinfo("Success", f"Account created for {entry_user.get().strip()}"))
           )
       )
).pack(pady=10)

root.mainloop()
