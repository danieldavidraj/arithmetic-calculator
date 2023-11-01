import tkinter as tk
import subprocess
import math

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def button_equals():
    expression = entry.get()
    try:
        result = subprocess.check_output(['./a.out', expression], text=True, stderr=subprocess.PIPE)
        output_label.config(text=f'Result: {result.strip()}')
    except subprocess.CalledProcessError as e:
        output_label.config(text=f'Error: {e.stderr.strip()}')

def button_function(func):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + func + '(')

def button_pi():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(math.pi))

def button_e():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(math.e))

def button_comma():
        current=entry.get()
        entry.delete(0,tk.END)
        entry.insert(0,current+',')

root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg='black')

entry = tk.Entry(root, width=20, font=('Arial', 16), bd=10, insertwidth=2, borderwidth=4, bg='white', justify='right')
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipadx=10, ipady=10)

buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0'
]

operators = [
    '/', '*', '-', '.', '+', '(', ')'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white',
              command=lambda button=button: button_click(button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

row_val = 1
col_val = 3
for button in operators:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white',
              command=lambda button=button: button_click(button)).grid(row=row_val, column=col_val)
    row_val += 1
    if row_val > 3:
        row_val = 1
        col_val += 1

tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: entry.delete(0, tk.END)).grid(row=3, column=5)
tk.Button(root, text='=', padx=30, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=button_equals).grid(row=6, column=5)

# Additional functions
tk.Button(root, text='sin', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('sin')).grid(row=4, column=0)
tk.Button(root, text='cos', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('cos')).grid(row=4, column=1)
tk.Button(root, text='tan', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('tan')).grid(row=4, column=2)
tk.Button(root, text='log', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('log')).grid(row=4, column=3)

tk.Button(root, text='asin', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('asin')).grid(row=4, column=4)
tk.Button(root, text='acos', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('acos')).grid(row=4, column=5)
tk.Button(root, text='atan', padx=15, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('atan')).grid(row=5, column=0)
tk.Button(root, text='sinh', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('sinh')).grid(row=5, column=1)
tk.Button(root, text='cosh', padx=15, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('cosh')).grid(row=5, column=2)
tk.Button(root, text='tanh', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('tanh')).grid(row=5, column=3)

tk.Button(root, text='pow', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('pow')).grid(row=5, column=4)
tk.Button(root, text='bin_dec', padx=10, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('bin_dec')).grid(row=5, column=5)
tk.Button(root, text='dec_bin', padx=5, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('dec_bin')).grid(row=6, column=0)
tk.Button(root, text='fact', padx=20, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=lambda: button_function('fact')).grid(row=6, column=1)

# Constants
tk.Button(root, text='π', padx=30, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=button_pi).grid(row=6, column=2)
tk.Button(root, text='e', padx=30, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=button_e).grid(row=6, column=3)
tk.Button(root, text=',', padx=30, pady=20, font=('Arial', 12), bd=8, bg='black', fg='white', command=button_comma).grid(row=6, column=4)

output_label = tk.Label(root, text="Result: ", font=('Arial', 14), bg='black', fg='white')
output_label.grid(row=7, column=0, columnspan=8)

root.mainloop()