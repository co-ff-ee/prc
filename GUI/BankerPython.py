from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Cab Booking")
root.geometry("320x250")

Label(root, text="Cab Booking", font=("Arial",14,"bold")).pack(pady=8)

Label(root, text="Name:").pack(anchor=W, padx=10)
e_name = Entry(root); e_name.pack(fill=X, padx=10)

Label(root, text="Pickup:").pack(anchor=W, padx=10)
e_pick = Entry(root); e_pick.pack(fill=X, padx=10)

Label(root, text="Drop:").pack(anchor=W, padx=10)
e_drop = Entry(root); e_drop.pack(fill=X, padx=10)

veh = StringVar(); veh.set("Auto")
OptionMenu(root, veh, "Auto", "Mini", "Sedan").pack(pady=8)

Button(root, text="Book", width=12,
       command=lambda: messagebox.showinfo(
           "Booked" if e_name.get().strip() and e_pick.get().strip() and e_drop.get().strip()
           else "Error",
           f"Booking for {e_name.get().strip() or 'N/A'}\n{e_pick.get().strip()} -> {e_drop.get().strip()}\nVehicle: {veh.get()}"
       )
).pack(pady=8)

root.mainloop()
