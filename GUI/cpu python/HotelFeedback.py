from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hotel Food Feedback")
root.geometry("350x400")

Label(root, text="Hotel Food Feedback Form", font=("Arial", 14, "bold")).pack(pady=10)

# Name and Email
Label(root, text="Customer Name:").pack(anchor=W, padx=20)
e_name = Entry(root, width=35)
e_name.pack(padx=20, pady=5)

Label(root, text="Email ID:").pack(anchor=W, padx=20)
e_email = Entry(root, width=35)
e_email.pack(padx=20, pady=5)

# Rating (Radiobuttons)
Label(root, text="Rate the Food Quality:").pack(anchor=W, padx=20, pady=5)
rating = IntVar()
Radiobutton(root, text="Excellent", variable=rating, value=5).pack(anchor=W, padx=40)
Radiobutton(root, text="Good", variable=rating, value=4).pack(anchor=W, padx=40)
Radiobutton(root, text="Average", variable=rating, value=3).pack(anchor=W, padx=40)
Radiobutton(root, text="Poor", variable=rating, value=2).pack(anchor=W, padx=40)

# Checkbuttons for liked aspects
Label(root, text="What did you like?").pack(anchor=W, padx=20, pady=5)
taste = IntVar()
service = IntVar()
clean = IntVar()
Checkbutton(root, text="Taste", variable=taste).pack(anchor=W, padx=40)
Checkbutton(root, text="Service", variable=service).pack(anchor=W, padx=40)
Checkbutton(root, text="Cleanliness", variable=clean).pack(anchor=W, padx=40)

# Comments box
Label(root, text="Additional Comments:").pack(anchor=W, padx=20, pady=5)
text = Text(root, height=4, width=35)
text.pack(padx=20)

# Submit button
Button(root, text="Submit Feedback", width=15,
       command=lambda: messagebox.showinfo(
           "Feedback Submitted",
           f"Name: {e_name.get()}\nEmail: {e_email.get()}\nRating: {rating.get()}\nLiked: "
           f"{'Taste ' if taste.get() else ''}"
           f"{'Service ' if service.get() else ''}"
           f"{'Cleanliness' if clean.get() else ''}\n"
           f"Comments: {text.get('1.0', END).strip()}"
       )
).pack(pady=15)

root.mainloop()
