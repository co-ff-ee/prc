from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Fund Transfer")
root.geometry("380x360")

Label(root, text="Fund Transfer", font=("Arial", 16, "bold")).pack(pady=10)

# From Account
Label(root, text="From Account Number:").pack(anchor=W, padx=20)
entry_from = Entry(root, width=30)
entry_from.pack(padx=20, pady=5)

# To Account
Label(root, text="To Account Number:").pack(anchor=W, padx=20)
entry_to = Entry(root, width=30)
entry_to.pack(padx=20, pady=5)

# Transfer Type
Label(root, text="Transfer Type:").pack(anchor=W, padx=20)
transfer_type = StringVar()
transfer_type.set("NEFT")
Radiobutton(root, text="NEFT", variable=transfer_type, value="NEFT").pack(anchor=W, padx=40)
Radiobutton(root, text="IMPS", variable=transfer_type, value="IMPS").pack(anchor=W, padx=40)
Radiobutton(root, text="RTGS", variable=transfer_type, value="RTGS").pack(anchor=W, padx=40)

# Amount
Label(root, text="Amount (INR):").pack(anchor=W, padx=20)
entry_amount = Entry(root, width=30)
entry_amount.pack(padx=20, pady=5)

# Remarks (Text)
Label(root, text="Remarks:").pack(anchor=W, padx=20)
text_remarks = Text(root, height=3, width=35)
text_remarks.pack(padx=20, pady=5)

# Confirm checkbox
confirm_var = IntVar()
Checkbutton(root, text="I confirm the above details", variable=confirm_var).pack(pady=8)

# Transfer Button (inline lambda shows a simple popup)
Button(root, text="Transfer", width=12,
       command=lambda: messagebox.showinfo(
           "Transfer",
           "Transfer Initiated!\nFrom: {}\nTo: {}\nAmount: ₹{}".format(
               entry_from.get(), entry_to.get(), entry_amount.get()
           ) if confirm_var.get() else "Please confirm the details before transfer."
       )
).pack(pady=10)

root.mainloop()
