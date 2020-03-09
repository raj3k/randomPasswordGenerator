import tkinter as tk
from tkinter import messagebox
import random

HEIGHT = 200
WIDTH = 500
dict = {
    "SMALL_LETTERS": "abcdefghijklmnopqrstuvwxyz",
    "NUMBERS": "0123456789",
    "BIG_LETTERS": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "CHAR": "!@#$%^&*()?"
}


root = tk.Tk()
root.resizable(width=False, height=False)
root.title('Password generator')


def check_entry(entry):
    if entry == '':
        return 0
    return entry


def password_generator(e1, e2, e3, e4):
    try:
        num_small_letters = int(check_entry(e1))
        num_numbers = int(check_entry(e2))
        num_big_letters = int(check_entry(e3))
        num_char = int(check_entry(e4))

        pass_len = num_small_letters + num_numbers + num_big_letters + num_char

        str = random.sample(dict["SMALL_LETTERS"], num_small_letters) + random.sample(dict["NUMBERS"], num_numbers) + random.sample(
            dict["BIG_LETTERS"], num_big_letters) + random.sample(dict["CHAR"], num_char)

        password = "".join(random.sample(str, pass_len))

        output.delete(0, "end")

        output.insert(0, password)
    except ValueError:
        messagebox.showerror('Error', 'Wrong input')


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, height=HEIGHT, width=WIDTH)
frame.place(relx=0.2, rely=0.1)


L1 = tk.Label(frame, text="Small letters")
L1.grid(row=0, column=0)
E1 = tk.Entry(frame)
E1.grid(row=0, column=1)

L2 = tk.Label(frame, text="Numbers")
L2.grid(row=1, column=0)
E2 = tk.Entry(frame)
E2.grid(row=1, column=1)

L3 = tk.Label(frame, text="Big letters")
L3.grid(row=2, column=0)
E3 = tk.Entry(frame)
E3.grid(row=2, column=1)

L4 = tk.Label(frame, text="Special characters")
L4.grid(row=3, column=0)
E4 = tk.Entry(frame)
E4.grid(row=3, column=1)

label = tk.Label(frame, text="Generated password")
label.grid(row=4, column=0)
output = tk.Entry(frame)
output.grid(row=4, column=1)


button = tk.Button(root, text="Submit", command=lambda: password_generator(E1.get(), E2.get(), E3.get(), E4.get()))
button.pack(side='bottom')

frame.mainloop()
