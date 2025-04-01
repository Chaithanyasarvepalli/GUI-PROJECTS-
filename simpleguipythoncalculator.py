import customtkinter as ctk
import time

# Initialize the app
ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("simple python Calculator")
app.geometry("300x400")
app.resizable(False, False)

# Entry widget for displaying expressions
expression = ""
def update_expression(value):
    global expression
    expression += str(value)
    entry_var.set(expression)

def clear_expression():
    global expression
    expression = ""
    entry_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    entry_var.set(expression)

def calculate_result():
    global expression
    try:
        result = str(eval(expression))  # Evaluate expression
        entry_var.set(result)
        expression = result  # Store result for further calculations
    except Exception:
        entry_var.set("Error")
        expression = ""

# Button animation effect
def button_animation(btn):
    original_color = btn.cget("fg_color")
    btn.configure(fg_color="#00ffcc")  # Glow effect
    app.update()
    time.sleep(0.1)
    btn.configure(fg_color=original_color)

# UI Elements
entry_var = ctk.StringVar()
entry = ctk.CTkEntry(app, textvariable=entry_var, font=("Arial", 20), width=280, height=40, justify='right', fg_color="#222831", text_color="white")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Button layout
buttons = [
    ('7', 1, 0, "#20b2aa"), ('8', 1, 1, "#20b2aa"), ('9', 1, 2, "#20b2aa"), ('/', 1, 3, "#001f3f"),
    ('4', 2, 0, "#20b2aa"), ('5', 2, 1, "#20b2aa"), ('6', 2, 2, "#20b2aa"), ('*', 2, 3, "#001f3f"),
    ('1', 3, 0, "#20b2aa"), ('2', 3, 1, "#20b2aa"), ('3', 3, 2, "#20b2aa"), ('-', 3, 3, "#001f3f"),
    ('0', 4, 0, "#20b2aa"), ('.', 4, 1, "#20b2aa"), ('+', 4, 2, "#001f3f"), ('=', 4, 3, "#008000")
]

for text, row, col, color in buttons:
    btn = ctk.CTkButton(app, text=text, width=65, height=50, fg_color=color, text_color="white", command=lambda t=text, b=color: [update_expression(t), button_animation(btn)])
    if text == "=":
        btn.configure(command=lambda b=btn: [calculate_result(), button_animation(b)])
    btn.grid(row=row, column=col, padx=3, pady=3)

# Clear and Backspace buttons
clear_btn = ctk.CTkButton(app, text="C", width=130, height=50, fg_color="#d90429", text_color="white", command=lambda: [clear_expression(), button_animation(clear_btn)])
clear_btn.grid(row=5, column=0, columnspan=2, padx=3, pady=6)

backspace_btn = ctk.CTkButton(app, text="⌫", width=130, height=50, fg_color="#808080", text_color="white", command=lambda: [backspace(), button_animation(backspace_btn)])
backspace_btn.grid(row=5, column=2, columnspan=2, padx=3, pady=6)

app.mainloop()
