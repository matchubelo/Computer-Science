import tkinter as tk
from tkinter import messagebox

# Logic
def OilLubeCharges():
    charges = 0
    if oil_change_var.get():
        charges += 26.00
    if lube_job_var.get():
        charges += 16.00
    return charges

def FlushCharges():
    charges = 0
    if radiator_flush_var.get():
        charges += 30.00
    if transmission_flush_var.get():
        charges += 80.00
    return charges

def MiscCharges():
    charges = 0
    if inspection_var.get():
        charges += 15.00
    if replace_muffler_var.get():
        charges += 100.00
    if tire_rotation_var.get():
        charges += 20.00
    return charges

def OtherCharges():
    try:
        parts_cost = float(parts_cost_entry.get()) if parts_cost_entry.get() else 0
        labor_cost = float(labor_cost_entry.get()) if labor_cost_entry.get() else 0
        labor_cost *= 20.00  # $20 per hour
        return parts_cost + labor_cost
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for parts and labor costs.")
        breakpoint

def Subtotal():
    
    return OilLubeCharges() + FlushCharges() + MiscCharges() + OtherCharges()

def Parts():
    try:
        return float(parts_cost_entry.get()) if parts_cost_entry.get() else 0
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for parts cost.")
        
        breakpoint  # Return 0 in case of invalid input

def Tax():
    parts_cost = Parts()
    tax = parts_cost * 0.0635  # Tax is only charged on parts
    return tax
def Labor():
    try:
        labor_cost = float(labor_cost_entry.get()) if labor_cost_entry.get() else 0
        return labor_cost * 20.00  # $20 per hour
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for labor hours.")
        breakpoint  # Return 0 in case of invalid input

def ServiceCharges():
    service_charges = OilLubeCharges() + FlushCharges() + MiscCharges() + Labor()
    return service_charges

def TotalCharges():

    subtotal = Subtotal()
    
    total = subtotal + Tax()
    # Display the results in the summary frame
    summary_text.set(f"Subtotal: ${subtotal:.2f}\nTax: ${Tax():.2f}\nTotal: ${total:.2f}")
    service_text.set(f"Service Charges: ${ServiceCharges():.2f}")
    parts_text.set(f"Parts Charges: ${Parts():.2f}")
    tax_text.set(f"Tax (parts): ${Tax():.2f}")


def ClearOilLube():
    oil_change_var.set(False)
    lube_job_var.set(False)

def ClearFlushes():
    radiator_flush_var.set(False)
    transmission_flush_var.set(False)

def ClearMisc():
    inspection_var.set(False)
    replace_muffler_var.set(False)
    tire_rotation_var.set(False)

def ClearOther():
    parts_cost_entry.delete(0, tk.END)
    labor_cost_entry.delete(0, tk.END)

def ClearFees():
    summary_text.set(
        "Subtotal: $0.00\n"
        "Tax: $0.00\n"
        "Total: $0.00"
        )
    service_text.set("Service Charges: $0.00")
    parts_text.set("Parts Charges: $0.00")
    tax_text.set("Tax (parts): $0.00")

def Clear():
    ClearOilLube()
    ClearFlushes()
    ClearMisc()
    ClearOther()
    ClearFees()

# GUI
window = tk.Tk()
window.title("Matt's Automotive")
window.geometry("725x600")
window.configure(bg="black")

# Oil & Lube
oil_lube_frame = tk.LabelFrame(window, text="Oil & Lube", bg="black", fg="white", font=("Arial", 12, "bold"))
oil_lube_frame.place(x=50, y=50, width=300, height=100)

oil_change_var = tk.BooleanVar()
oil_change_checkbox = tk.Checkbutton(oil_lube_frame, text="Oil Change ($26.00)", variable=oil_change_var, bg="black", fg="white", font=("Arial", 10))
oil_change_checkbox.pack(anchor="w", padx=10, pady=5)

lube_job_var = tk.BooleanVar()
lube_job_checkbox = tk.Checkbutton(oil_lube_frame, text="Lube Job ($16.00)", variable=lube_job_var, bg="black", fg="white", font=("Arial", 10))
lube_job_checkbox.pack(anchor="w", padx=10, pady=5)

# Flushes
flush_frame = tk.LabelFrame(window, text="Flushes", bg="black", fg="white", font=("Arial", 12, "bold"))
flush_frame.place(x=375, y=50, width=300, height=100)

radiator_flush_var = tk.BooleanVar()
radiator_flush_checkbox = tk.Checkbutton(flush_frame, text="Radiator Flush ($30.00)", variable=radiator_flush_var, bg="black", fg="white", font=("Arial", 10))
radiator_flush_checkbox.pack(anchor="w", padx=10, pady=5)

transmission_flush_var = tk.BooleanVar()
transmission_flush_checkbox = tk.Checkbutton(flush_frame, text="Transmission Flush ($80.00)", variable=transmission_flush_var, bg="black", fg="white", font=("Arial", 10))
transmission_flush_checkbox.pack(anchor="w", padx=10, pady=5)

# Miscellaneous
misc_frame = tk.LabelFrame(window, text="Misc", bg="black", fg="white", font=("Arial", 12, "bold"))
misc_frame.place(x=50, y=175, width=300, height=100)

inspection_var = tk.BooleanVar()
inspection_checkbox = tk.Checkbutton(misc_frame, text="Inspection ($15.00)", variable=inspection_var, bg="black", fg="white", font=("Arial", 10))
inspection_checkbox.pack(anchor="w", padx=10, pady=5)

replace_muffler_var = tk.BooleanVar()
replace_muffler_checkbox = tk.Checkbutton(misc_frame, text="Replace Muffler ($100.00)", variable=replace_muffler_var, bg="black", fg="white", font=("Arial", 10))
replace_muffler_checkbox.pack(anchor="w", padx=10, pady=5)

tire_rotation_var = tk.BooleanVar()
tire_rotation_checkbox = tk.Checkbutton(misc_frame, text="Tire Rotation ($20.00)", variable=tire_rotation_var, bg="black", fg="white", font=("Arial", 10))
tire_rotation_checkbox.pack(anchor="w", padx=10, pady=5)

# Parts & Labor
parts_labor_frame = tk.LabelFrame(window, text="Parts & Labor", bg="black", fg="white", font=("Arial", 12, "bold"))
parts_labor_frame.place(x=375, y=175, width=300, height=100)

parts_cost_label = tk.Label(parts_labor_frame, text="Parts Cost ($):", bg="black", fg="white", font=("Arial", 10))
parts_cost_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")

parts_cost_entry = tk.Entry(parts_labor_frame, bg="white", fg="black", font=("Arial", 10))
parts_cost_entry.grid(row=0, column=1, padx=5, pady=2, sticky="e")

labor_cost_label = tk.Label(parts_labor_frame, text="Labor Cost (Hours):", bg="black", fg="white", font=("Arial", 10))
labor_cost_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")

labor_cost_entry = tk.Entry(parts_labor_frame, bg="white", fg="black", font=("Arial", 10))
labor_cost_entry.grid(row=1, column=1, padx=5, pady=2, sticky="e")

parts_labor_frame.grid_columnconfigure(0, weight=1)
parts_labor_frame.grid_columnconfigure(1, weight=1)

# Summary
summary_frame = tk.LabelFrame(window, text="Summary", bg="black", fg="white", font=("Arial", 12, "bold"))
summary_frame.place(x=50, y=300, width=625, height=250)

summary_text = tk.StringVar()
summary_label = tk.Label(summary_frame, textvariable=summary_text, bg="black", fg="white", font=("Arial", 12, "bold"), justify="left")
summary_text.set(
        "Subtotal: $0.00\n"
        "Tax: $0.00\n"
        "Total: $0.00"
        )
summary_label.pack(padx=10, pady=10, anchor="w")

service_text = tk.StringVar()
service_label = tk.Label(summary_frame, textvariable=service_text, bg="black", fg="white", font=("Arial", 12, "bold"))
service_text.set("Service Charges: $0.00")
service_label.place(x=400, y=10)

parts_text = tk.StringVar()
parts_label = tk.Label(summary_frame, textvariable=parts_text, bg="black", fg="white", font=("Arial", 12, "bold"))
parts_text.set("Parts Charges: $0.00")
parts_label.place(x=400, y=40)

tax_text = tk.StringVar()
tax_label = tk.Label(summary_frame, textvariable=tax_text, bg="black", fg="white", font=("Arial", 12, "bold"))
tax_text.set("Tax (parts): $0.00")
tax_label.place(x=400, y=70)



# Buttons
button_width = 100
button_height = 30
button_spacing = (625 - (3 * button_width)) // 4

calculate_button = tk.Button(window, text="Calculate", command=TotalCharges, bg="white", fg="black", font=("Arial", 12))
calculate_button.place(x=50 + button_spacing, y=535, width=button_width, height=button_height)

clear_button = tk.Button(window, text="Clear", command=Clear, bg="white", fg="black", font=("Arial", 12))
clear_button.place(x=50 + button_spacing * 2 + button_width, y=535, width=button_width, height=button_height)

exit_button = tk.Button(window, text="Exit", command=window.quit, bg="white", fg="black", font=("Arial", 12))
exit_button.place(x=50 + button_spacing * 3 + button_width * 2, y=535, width=button_width, height=button_height)

window.mainloop()