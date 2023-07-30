import tkinter
from tkinter import *
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length < 6:
        password_label.config(text="Password length should be at least 6 characters!")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_label.config(text=f"Generated Password: {password}")

# Create the main application window
root = Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create widgets
length_label = Label(root, text="Enter password length:")
length_label.pack(pady=10)

length_entry = Entry(root)
length_entry.pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

password_label = Label(root, text="")
password_label.pack()

# Start the application event loop
root.mainloop()
