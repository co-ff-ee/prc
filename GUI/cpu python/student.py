from tkinter import *

root = Tk()
root.title("Student Registration Form")
root.geometry("400x520")

Label(root, text="Student Registration Form", font=("Arial", 14, "bold")).pack(pady=10)

# Student Name
Label(root, text="Full Name:").pack()
entry_name = Entry(root, width=40)
entry_name.pack(pady=5)

# Roll Number
Label(root, text="Roll Number:").pack()
entry_roll = Entry(root, width=40)
entry_roll.pack(pady=5)

# Gender
Label(root, text="Gender:").pack()
gender = StringVar()
Radiobutton(root, text="Male", variable=gender, value="Male").pack()
Radiobutton(root, text="Female", variable=gender, value="Female").pack()

# Address
Label(root, text="Address:").pack()
text_address = Text(root, height=3, width=35)
text_address.pack(pady=5)

# Course Selection (Listbox)
Label(root, text="Select Course:").pack()
course_list = Listbox(root, height=5)
courses = ["Computer Engineering", "IT", "Mechanical", "Electrical", "Civil"]
for c in courses:
    course_list.insert(END, c)
course_list.pack(pady=5)

# Subjects (Checkbuttons)
Label(root, text="Select Subjects:").pack()
cb1 = Checkbutton(root, text="Mathematics")
cb1.pack(anchor=W)
cb2 = Checkbutton(root, text="Physics")
cb2.pack(anchor=W)
cb3 = Checkbutton(root, text="Chemistry")
cb3.pack(anchor=W)
cb4 = Checkbutton(root, text="Programming")
cb4.pack(anchor=W)

# Phone Number
Label(root, text="Phone Number:").pack()
entry_phone = Entry(root, width=40)
entry_phone.pack(pady=5)

# Email ID
Label(root, text="Email ID:").pack()
entry_email = Entry(root, width=40)
entry_email.pack(pady=5)

# Submit Button
Button(root, text="Submit", width=12).pack(pady=15)

root.mainloop()
