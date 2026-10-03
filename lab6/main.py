"""
Laboratory Activity: Professional Tkinter App Shell & Window Hierarchy
Course : Python Programming with Tkinter
Group  : GroupName  (change this!)

WINDOW HIERARCHY
    Tk()  ->  root  (PARENT / main window)
                |-- Toplevel(root)  -> New Window   (CHILD)
                |-- Toplevel(root)  -> About Window (CHILD)
"""

import tkinter as tk
from tkinter import messagebox

# ------------------------------------------------------------------
# CONFIGURATION (edit these to match your group)
# ------------------------------------------------------------------
APP_NAME = "Café Management System"
GROUP_NAME = "Group 3"
COURSE = "Python Programming"
TECHNOLOGY = "Python Tkinter"
VERSION = "1.0"
YEAR = "2026"
DESCRIPTION = "A professional application shell for managing cafe\norders, menu items and customers. It can be expanded later."

BG = "#f6ede3"       
ACCENT = "#6f4e37"   


# ------------------------------------------------------------------
# MEMBER 3 - TOPLEVEL DEVELOPER: New window
# ------------------------------------------------------------------
def open_new_window():
    """File -> New : creates a child Toplevel of the main window."""
    new_window = tk.Toplevel(root)          
    new_window.title("New Order")
    new_window.geometry("400x360")
    new_window.configure(bg=BG)
    new_window.resizable(False, False)
    new_window.transient(root)              

    tk.Label(new_window, text="Create a new cafe order here.",
             font=("Segoe UI", 13), bg=BG).pack(pady=(15, 10))

    form = tk.Frame(new_window, bg=BG)
    form.pack(padx=20, fill="x")

    tk.Label(form, text="Customer Name:", bg=BG).grid(row=0, column=0, sticky="w", pady=5)
    tk.Entry(form, width=26).grid(row=0, column=1, pady=5)

    tk.Label(form, text="Menu Item:", bg=BG).grid(row=1, column=0, sticky="w", pady=5)
    item = tk.StringVar(value="Cappuccino")
    tk.OptionMenu(form, item, "Espresso", "Cappuccino", "Latte", "Iced Tea",
                  "Croissant", "Cheesecake").grid(row=1, column=1, sticky="w", pady=5)

    tk.Label(form, text="Quantity:", bg=BG).grid(row=2, column=0, sticky="w", pady=5)
    tk.Spinbox(form, from_=1, to=20, width=5).grid(row=2, column=1, sticky="w", pady=5)

    tk.Label(form, text="Notes:", bg=BG).grid(row=3, column=0, sticky="nw", pady=5)
    tk.Text(form, width=20, height=4).grid(row=3, column=1, pady=5)

    def save_order():
        
        messagebox.showinfo("Save", "Order saved! (demo only - nothing is recorded)",
                            parent=new_window)

    buttons = tk.Frame(new_window, bg=BG)
    buttons.pack(pady=15)
    tk.Button(buttons, text="[ Save ]", bg=ACCENT, fg="white",
              width=12, command=save_order).pack(side="left", padx=6)
    tk.Button(buttons, text="[ Close ]", bg=ACCENT, fg="white",
              width=12, command=new_window.destroy).pack(side="left", padx=6)


# ------------------------------------------------------------------
# MEMBER 4 - ABOUT DIALOG DEVELOPER: About window
# ------------------------------------------------------------------
about_window = None   


def open_about_window():
    """File -> About : creates a child Toplevel of the main window."""
    global about_window
    if about_window is not None and about_window.winfo_exists():
        about_window.lift()                 
        return

    about_window = tk.Toplevel(root)        
    about_window.title("About")
    about_window.geometry("420x330")
    about_window.configure(bg=BG)
    about_window.resizable(False, False)
    about_window.transient(root)

    tk.Label(about_window, text="About Our Application",
             font=("Segoe UI", 16, "bold"), fg=ACCENT, bg=BG).pack(pady=(18, 10))

    info = [
        ("Application Name:", APP_NAME),
        ("Developed by:", GROUP_NAME),
        ("Course:", COURSE),
        ("Technology:", TECHNOLOGY),
        ("Version:", VERSION),
    ]
    for label, value in info:
        row = tk.Frame(about_window, bg=BG)
        row.pack(anchor="w", padx=30, pady=2)
        tk.Label(row, text=label, font=("Segoe UI", 10, "bold"), bg=BG).pack(side="left")
        tk.Label(row, text=" " + value, font=("Segoe UI", 10), bg=BG).pack(side="left")

    tk.Label(about_window, text=DESCRIPTION, bg=BG, fg="#444").pack(pady=10)
    tk.Label(about_window, text=f"Copyright © {YEAR} {GROUP_NAME}",
             font=("Segoe UI", 8), bg=BG, fg="#666").pack()

    tk.Button(about_window, text="[ Close ]", bg=ACCENT, fg="white",
              width=16, command=about_window.destroy).pack(pady=15)


# ------------------------------------------------------------------
# MEMBER 2 - MENU DEVELOPER: Exit command
# ------------------------------------------------------------------
def exit_app():
    """File -> Exit : closes the main window (and its children)."""
    root.destroy()


# ------------------------------------------------------------------
# MEMBER 1 - MAIN WINDOW DEVELOPER: Tk() root, layout
# ------------------------------------------------------------------
root = tk.Tk()                              
root.title("Application")
root.geometry("520x300")
root.configure(bg=BG)

tk.Label(root, text=APP_NAME.upper(), font=("Segoe UI", 18, "bold"),
         fg=ACCENT, bg=BG).pack(pady=(50, 10))
tk.Label(root, text="Welcome to our application!",
         font=("Segoe UI", 11), bg=BG).pack(pady=5)
tk.Button(root, text="[ Open New Window ]", font=("Segoe UI", 10),
          bg=ACCENT, fg="white", padx=10, pady=4,
          command=open_new_window).pack(pady=20)

# ------------------------------------------------------------------
# MEMBER 2 - MENU DEVELOPER: Menu bar and File menu
# ------------------------------------------------------------------
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=open_new_window)
file_menu.add_command(label="About", command=open_about_window)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

root.mainloop()