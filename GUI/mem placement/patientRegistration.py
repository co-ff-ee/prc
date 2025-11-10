from tkinter import *

root = Tk()
root.title("Patient Registration Form")
root.geometry("400x500")

Label(root, text="Hospital Patient Registration", font=("Arial", 14, "bold")).pack(pady=10)

# Name
Label(root, text="Full Name:").pack()
entry_name = Entry(root, width=40)
entry_name.pack(pady=5)

# Age
Label(root, text="Age:").pack()
entry_age = Entry(root, width=40)
entry_age.pack(pady=5)

# Gender
Label(root, text="Gender:").pack()
gender = StringVar()
Radiobutton(root, text="Male", variable=gender, value="Male").pack()
Radiobutton(root, text="Female", variable=gender, value="Female").pack()

# Symptoms (Text box)
Label(root, text="Symptoms / Health Issue:").pack()
text_symptom = Text(root, height=4, width=35)
text_symptom.pack(pady=5)

# Department (Listbox)
Label(root, text="Select Department:").pack()
listbox = Listbox(root, height=5)
departments = ["General Medicine", "Cardiology", "Orthopedics", "Pediatrics", "Dermatology"]
for d in departments:
    listbox.insert(END, d)
listbox.pack(pady=5)

# Facilities (Checkbuttons)
Label(root, text="Facilities Required:").pack()
cb1 = Checkbutton(root, text="Wheelchair")
cb1.pack(anchor=W)
cb2 = Checkbutton(root, text="Ambulance Service")
cb2.pack(anchor=W)
cb3 = Checkbutton(root, text="Private Room")
cb3.pack(anchor=W)

# Submit Button
Button(root, text="Submit", width=12).pack(pady=15)

root.mainloop()
