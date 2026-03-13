import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "add":
            res = num1 + num2
            result_label.config(text=f"The sum of {num1} + {num2} is {res}")
        elif operation == "subtract":
            res = num1 - num2
            result_label.config(text=f"The difference of {num1} - {num2} is {res}")
        elif operation == "multiply":
            res = num1 * num2
            result_label.config(text=f"The product of {num1} * {num2} is {res}")
        elif operation == "division":
            if num2 == 0:
                result_label.config(text="Error: Cannot divide by zero")
            else:
                res = num1 / num2
                result_label.config(text=f"The quotient of {num1} / {num2} is {res}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x250")
root.configure(bg="pink")

result_label = tk.Label(root, text="Enter numbers and click a button", bg="white", fg="black")
result_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

frame = tk.Frame(root, bg="pink")
frame.grid(row=1, column=0, columnspan=2, padx=20)

tk.Label(frame, text="Enter 1st Number:", bg="pink").grid(row=0, column=0, pady=5, sticky="e")
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Enter 2nd Number:", bg="pink").grid(row=1, column=0, pady=5, sticky="e")
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, pady=5)

tk.Button(frame, text="Add", width=10, command=lambda: calculate("add")).grid(row=2, column=0, pady=10)
tk.Button(frame, text="Subtract", width=10, command=lambda: calculate("subtract")).grid(row=2, column=1, pady=10)
tk.Button(frame, text="Multiply", width=10, command=lambda: calculate("multiply")).grid(row=3, column=0, pady=10)
tk.Button(frame, text="Divide", width=10, command=lambda: calculate("division")).grid(row=3, column=1, pady=10)

root.mainloop()
