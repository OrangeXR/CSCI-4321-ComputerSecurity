import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import threading
import re
import webbrowser
from blackbird import run_blackbird_search

# Globals to hold last search results
last_results = []
last_mode = None

def run_username_search():
    query = username_entry.get().strip()
    if not query:
        return
    start_search(username=query)

def run_email_search():
    query = email_entry.get().strip()
    if not query:
        return
    if not is_valid_email(query):
        messagebox.showerror("Invalid Email", f"'{query}' is not a valid email address.")
        return
    start_search(email=query)

def start_search(username=None, email=None):
    progress_var.set(0)
    status_label.config(text="Searching...")

    # Collect options from checkboxes
    options = []
    if verbose_var.get():
        options.append("--verbose")
    if permute_var.get():
        options.append("--permute")
    if permuteall_var.get():
        options.append("--permuteall")
    if no_nsfw_var.get():
        options.append("--no-nsfw")
    if filter_var.get():
        filter_arg = filter_entry.get().strip()
        if filter_arg:
            options.append(f'--filter {filter_arg}')

    threading.Thread(target=do_search, args=(username, email, options), daemon=True).start()

def do_search(username=None, email=None, options=None):
    global last_results, last_mode
    last_results = run_blackbird_search(username=username, email=email, options=options)
    last_mode = "username" if username else "email"

    total = len(last_results) if last_results else 1
    for i, _ in enumerate(last_results or []):
        percent = int((i + 1) / total * 100)
        progress_var.set(percent)
        root.update_idletasks()

    display_results(last_results)
    status_label.config(text="Search complete")

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def display_results(results):
    for item in tree.get_children():
        tree.delete(item)
    for row in results or []:
        tree.insert("", "end", values=(
            row.get("name", ""),
            row.get("url", ""),
            row.get("status", "")
        ))

def on_row_double_click(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    item = tree.item(selected_item)
    values = item.get("values", [])
    if len(values) >= 2:
        url = values[1]
        if url:
            webbrowser.open_new_tab(url)

root = tk.Tk()
root.title("Blackbird GUI")
root.geometry("900x700")

# Load background image
bg_image = Image.open("blackbird.png")  # Replace with your actual image path
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=900, height=700)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Username
username_label = tk.Label(root, text="Username:", bg="white")
username_entry = tk.Entry(root, width=50)
username_btn = tk.Button(root, text="Search Username", command=run_username_search)

canvas.create_window(100, 30, window=username_label, anchor="nw")
canvas.create_window(100, 55, window=username_entry, anchor="nw")
canvas.create_window(100, 85, window=username_btn, anchor="nw")

# Email
email_label = tk.Label(root, text="Email:", bg="white")
email_entry = tk.Entry(root, width=50)
email_btn = tk.Button(root, text="Search Email", command=run_email_search)

canvas.create_window(100, 125, window=email_label, anchor="nw")
canvas.create_window(100, 150, window=email_entry, anchor="nw")
canvas.create_window(100, 180, window=email_btn, anchor="nw")

# Options
options_label = tk.Label(root, text="Search Options:", bg="white")
canvas.create_window(100, 220, window=options_label, anchor="nw")

verbose_var = tk.BooleanVar()
permute_var = tk.BooleanVar()
permuteall_var = tk.BooleanVar()
no_nsfw_var = tk.BooleanVar()
filter_var = tk.BooleanVar()

canvas.create_window(100, 245, window=tk.Checkbutton(root, text="--verbose", variable=verbose_var, bg="white"), anchor="nw")
canvas.create_window(100, 270, window=tk.Checkbutton(root, text="--permute", variable=permute_var, bg="white"), anchor="nw")
canvas.create_window(100, 295, window=tk.Checkbutton(root, text="--permuteall", variable=permuteall_var, bg="white"), anchor="nw")
canvas.create_window(100, 320, window=tk.Checkbutton(root, text="--no-nsfw", variable=no_nsfw_var, bg="white"), anchor="nw")
canvas.create_window(100, 345, window=tk.Checkbutton(root, text="--filter", variable=filter_var, bg="white"), anchor="nw")

filter_entry = tk.Entry(root, width=60)
filter_entry.insert(0, 'e.g. name=twitter or cat~social')
canvas.create_window(100, 370, window=filter_entry, anchor="nw")

# Progress bar + status
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
status_label = tk.Label(root, text="Idle", bg="white")

canvas.create_window(100, 410, window=progress_bar, anchor="nw", width=700)
canvas.create_window(100, 440, window=status_label, anchor="nw")

# Table frame
table_frame = tk.Frame(root)
canvas.create_window(100, 470, window=table_frame, anchor="nw", width=700, height=200)

scroll_y = tk.Scrollbar(table_frame, orient="vertical")
scroll_x = tk.Scrollbar(table_frame, orient="horizontal")

tree = ttk.Treeview(
    table_frame,
    columns=("Site", "URL", "Status"),
    show="headings",
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)
tree.heading("Site", text="Site")
tree.column("Site", width=200, anchor="w")
tree.heading("URL", text="URL")
tree.column("URL", width=400, anchor="w")
tree.heading("Status", text="Status")
tree.column("Status", width=120, anchor="center")

scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)

scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
tree.pack(expand=True, fill="both")

tree.bind("<Double-1>", on_row_double_click)

root.mainloop()




# ==========================================================================================================

# What You Need
# • 	Save the blackbird image as  in the same folder as your script.
# • 	Install Pillow if you haven’t already:


# pip install pillow
