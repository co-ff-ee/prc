from tkinter import *

root = Tk()
root.title("Online Quiz")
root.geometry("350x380")

Label(root, text="Online Quiz", font=("Arial", 16, "bold")).pack(pady=10)

# Question 1
Label(root, text="1. What is the capital of India?").pack(anchor=W, padx=20)
q1 = IntVar()
Radiobutton(root, text="Delhi", variable=q1, value=1).pack(anchor=W, padx=40)
Radiobutton(root, text="Mumbai", variable=q1, value=2).pack(anchor=W, padx=40)
Radiobutton(root, text="Chennai", variable=q1, value=3).pack(anchor=W, padx=40)

# Question 2
Label(root, text="2. Which language is used for AI?").pack(anchor=W, padx=20, pady=5)
q2 = IntVar()
Radiobutton(root, text="Python", variable=q2, value=1).pack(anchor=W, padx=40)
Radiobutton(root, text="HTML", variable=q2, value=2).pack(anchor=W, padx=40)
Radiobutton(root, text="C", variable=q2, value=3).pack(anchor=W, padx=40)

# Question 3
Label(root, text="3. What is 5 + 3 ?").pack(anchor=W, padx=20, pady=5)
q3 = IntVar()
Radiobutton(root, text="8", variable=q3, value=1).pack(anchor=W, padx=40)
Radiobutton(root, text="9", variable=q3, value=2).pack(anchor=W, padx=40)
Radiobutton(root, text="7", variable=q3, value=3).pack(anchor=W, padx=40)

# Comments
Label(root, text="Comments:").pack(anchor=W, padx=20, pady=5)
text = Text(root, height=3, width=30)
text.pack()

Button(root, text="Submit", width=10).pack(pady=10)

root.mainloop()
