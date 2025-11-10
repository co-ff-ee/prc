from tkinter import *

root = Tk()
root.title("Sports Academy Registration Form")
root.geometry("350x400")

title = Label(root, text="Sports Academy Registration", font=("Arial", 14, "bold"))
title.pack(pady=10)

# Labels and Entry boxes
Label(root, text="Full Name:").pack()
entry_name = Entry(root, width=30)
entry_name.pack(pady=5)

Label(root, text="Age:").pack()
entry_age = Entry(root, width=30)
entry_age.pack(pady=5)

Label(root, text="Gender:").pack()
gender = StringVar()
Radiobutton(root, text="Male", variable=gender, value="Male").pack()
Radiobutton(root, text="Female", variable=gender, value="Female").pack()

Label(root, text="Select Sport:").pack()
sport = StringVar()
menu = OptionMenu(root, sport, "Cricket", "Football", "Badminton", "Swimming", "Tennis")
menu.pack(pady=5)

Label(root, text="Phone Number:").pack()
entry_phone = Entry(root, width=30)
entry_phone.pack(pady=5)

Label(root, text="Email ID:").pack()
entry_email = Entry(root, width=30)
entry_email.pack(pady=5)

Button(root, text="Submit", width=10).pack(pady=15)

root.mainloop()
