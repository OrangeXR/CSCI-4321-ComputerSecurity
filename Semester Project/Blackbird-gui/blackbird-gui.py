
import tkinter as tk
from tkinter import ttk, messagebox
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

    # Collect --filter argument if enabled
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

# Username search
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root, width=50)
username_entry.pack(pady=5)
username_btn = tk.Button(root, text="Search Username", command=run_username_search)
username_btn.pack(pady=5)

# Email search
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)
email_btn = tk.Button(root, text="Search Email", command=run_email_search)
email_btn.pack(pady=5)

# Options
options_label = tk.Label(root, text="Search Options:")
options_label.pack(pady=5)

verbose_var = tk.BooleanVar()
permute_var = tk.BooleanVar()
permuteall_var = tk.BooleanVar()
no_nsfw_var = tk.BooleanVar()
filter_var = tk.BooleanVar()

tk.Checkbutton(root, text="--verbose", variable=verbose_var).pack(anchor="w")
tk.Checkbutton(root, text="--permute", variable=permute_var).pack(anchor="w")
tk.Checkbutton(root, text="--permuteall", variable=permuteall_var).pack(anchor="w")
tk.Checkbutton(root, text="--no-nsfw", variable=no_nsfw_var).pack(anchor="w")

tk.Checkbutton(root, text="--filter", variable=filter_var).pack(anchor="w")
filter_entry = tk.Entry(root, width=60)
filter_entry.insert(0, 'e.g. name=twitter or cat~social')
filter_entry.pack(pady=2)

# Progress bar + status
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill="x", pady=5)
status_label = tk.Label(root, text="Idle")
status_label.pack()

# Frame for table + scrollbar
table_frame = tk.Frame(root)
table_frame.pack(expand=True, fill="both", pady=10)

scroll_y = tk.Scrollbar(table_frame, orient="vertical")
scroll_x = tk.Scrollbar(table_frame, orient="horizontal")

tree = ttk.Treeview(
    table_frame,
    columns=("Site", "URL", "Status"),
    show="headings",
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)
# for col in ("Site", "URL", "Status"):
#     tree.heading(col, text=col)
#     tree.column(col, width=250, anchor="w")
tree.heading("Site", text="Site")
tree.column("Site", width=100, anchor="w")

tree.heading("URL", text="URL")
tree.column("URL", width=560, anchor="w")   # wider

tree.heading("Status", text="Status")
tree.column("Status", width=60, anchor="w")  # narrower



scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)

scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
tree.pack(expand=True, fill="both")

tree.bind("<Double-1>", on_row_double_click)

root.mainloop()
