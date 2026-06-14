import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Matt's Calculator")



# Create a 0 widget
button0 = tk.Button(
    text="0",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 1 widget
button1 = tk.Button(
    text="1",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 2 widget
button2 = tk.Button(
    text="2",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 3 widget
button3 = tk.Button(
    text="3",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 4 widget
button4 = tk.Button(
    text="4",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 5 widget
button5 = tk.Button(
    text="5",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 6 widget
button6 = tk.Button(
    text="6",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 7 widget
button7 = tk.Button(
    text="7",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 8 widget
button8 = tk.Button(
    text="8",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a 9 widget
button9 = tk.Button(
    text="9",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a multiply widget
buttonmultiply = tk.Button(
    text="X",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a divide widget
buttondivide = tk.Button(
    text="/",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a add widget
buttonadd = tk.Button(
    text="+",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a subtract widget
buttonsubtract = tk.Button(
    text="-",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a equal widget
buttonequal = tk.Button(
    text="=",
    width=10,
    height=10,
    bg="white",
    fg="black",
)

# Create a clear widget
buttonclear = tk.Button(
    text="Clear",
    width=10,
    height=10,
    bg="white",
    fg="black",
)



# Places the widgets on the window
button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=0, column=2, padx=5, pady=5)
button4.grid(row=1, column=0, padx=5, pady=5)
button5.grid(row=1, column=1, padx=5, pady=5)
button6.grid(row=1, column=2, padx=5, pady=5)
button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button9.grid(row=2, column=2, padx=5, pady=5)
button0.grid(row=3, column=1, padx=5, pady=5)

buttonmultiply.grid(row=0, column=3, padx=5, pady=5)
buttondivide.grid(row=1, column=3, padx=5, pady=5)
buttonadd.grid(row=2, column=3, padx=5, pady=5)
buttonsubtract.grid(row=3, column=3, padx=5, pady=5)

buttonequal.grid(row=3, column=2, padx=5, pady=5)
buttonclear.grid(row=3, column=0, padx=5, pady=5)

entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=4, column=0, columnspan=4, padx=10, pady=10)


# Define button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Define clear function
def button_clear():
    entry.delete(0, tk.END)

# Define add function
def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, tk.END)

# Define subtract function
def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, tk.END)

# Define multiply function
def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, tk.END)

# Define divide function
def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, tk.END)

# Define equal function
def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    elif math == "division":
        entry.insert(0, f_num / int(second_number))

# Assign functions to buttons
button0.config(command=lambda: button_click(0))
button1.config(command=lambda: button_click(1))
button2.config(command=lambda: button_click(2))
button3.config(command=lambda: button_click(3))
button4.config(command=lambda: button_click(4))
button5.config(command=lambda: button_click(5))
button6.config(command=lambda: button_click(6))
button7.config(command=lambda: button_click(7))
button8.config(command=lambda: button_click(8))
button9.config(command=lambda: button_click(9))

buttonadd.config(command=button_add)
buttonsubtract.config(command=button_subtract)
buttonmultiply.config(command=button_multiply)
buttondivide.config(command=button_divide)
buttonequal.config(command=button_equal)
buttonclear.config(command=button_clear)


# Start the Tkinter event loop
window.mainloop()