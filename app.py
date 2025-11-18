import tkinter as tk
from tkinter import ttk

C1 = " A: change of structure"
C2 = " B: liquidity grab"
C3 = " C: fake run"
C4 = " D: sprint"

# Create main window
window = tk.Tk()
window.title("Select Confirmations")
window.configure(bg='black')

# Configure style for dark theme
style = ttk.Style()
style.theme_use('default')
style.configure('TCheckbutton', 
                background='black', 
                foreground='white',
                font=('Arial', 10))
style.map('TCheckbutton',
          background=[('active', 'black')],
          foreground=[('active', 'white')])
style.configure('TLabel',
                background='black',
                foreground='white',
                font=('Arial', 10))

# Variables to track checkboxes
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()

# Create checkboxes
checkbox1 = ttk.Checkbutton(window, text=C1, variable=var1, style='TCheckbutton')
checkbox2 = ttk.Checkbutton(window, text=C2, variable=var2, style='TCheckbutton')
checkbox3 = ttk.Checkbutton(window, text=C3, variable=var3, style='TCheckbutton')
checkbox4 = ttk.Checkbutton(window, text=C4, variable=var4, style='TCheckbutton')

# Position checkboxes in window
checkbox1.pack(anchor='w', padx=10, pady=5)
checkbox2.pack(anchor='w', padx=10, pady=5)
checkbox3.pack(anchor='w', padx=10, pady=5)
checkbox4.pack(anchor='w', padx=10, pady=5)

# Label to show result
result = ttk.Label(window, text="", style='TLabel')
result.pack(pady=10)

# Start GUI loop
window.mainloop()