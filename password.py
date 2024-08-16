import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        label_password.config(text=f"Generated Password: {password}")
    except ValueError as ve:
        label_password.config(text=f"Error: {ve}")

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter the desired password length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack()

label_password = tk.Label(root, text="Generated Password:")
label_password.pack()

root.mainloop()