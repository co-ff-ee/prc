from tkinter import *

root = Tk()
root.title("Help Screen")
root.geometry("350x250")

Label(root, text="Help - Application Support", font=("Arial", 14, "bold")).pack(pady=10)

help_text = """If you face any issues while using this app:
1. Make sure you have a stable internet connection.
2. Restart the application.
3. Check the user manual for guidance.
4. For further help, contact:
   support@example.com
"""

Label(root, text=help_text, justify=LEFT, padx=10).pack()

Button(root, text="Close", width=10, command=root.destroy).pack(pady=10)

root.mainloop()
