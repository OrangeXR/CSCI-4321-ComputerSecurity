import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import re
import webbrowser
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdf_canvas
from blackbird import run_blackbird_search

# =============================================================================================================================
# Globals to hold last search results
last_results = []
last_mode = None
last_phrase = None
search_results_by_phrase = {}

# =============================================================================================================================
# ======================================= username search =====================================================================

def run_username_search():
    query = username_entry.get().strip()
    if not query:
        return
    # Allow multiple usernames separated by commas
    usernames = [name.strip() for name in query.split(",") if name.strip()]
    if usernames:
        start_search(usernames=usernames)

# ======================================= email search with validation ========================================================

def run_email_search():
    query = email_entry.get().strip()
    if not query:
        return
    # Allow multiple emails separated by commas
    emails = [e.strip() for e in query.split(",") if e.strip()]
    invalids = [e for e in emails if not is_valid_email(e)]
    if invalids:
        messagebox.showerror("Invalid Email(s)", f"These are not valid: {', '.join(invalids)}")
        return
    if emails:
        start_search(emails=emails)

# ======================================= prepare search ======================================================================

def start_search(usernames=None, emails=None):
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

    threading.Thread(target=do_search, args=(usernames, emails, options), daemon=True).start()

# ======================================= search logic ===========================================================================

def do_search(usernames=None, emails=None, options=None):
    global last_results, last_mode, last_phrase, search_results_by_phrase
    last_results = []
    search_results_by_phrase = {}
    last_phrase = None

    if usernames:
        last_mode = "username"
        last_phrase = ", ".join(usernames)
        for name in usernames:
            results = run_blackbird_search(username=name, options=options)
            if results:
                search_results_by_phrase[name] = results
                last_results.extend(results)
    elif emails:
        last_mode = "email"
        last_phrase = ", ".join(emails)
        for e in emails:
            results = run_blackbird_search(email=e, options=options)
            if results:
                search_results_by_phrase[e] = results
                last_results.extend(results)

    total = len(last_results) if last_results else 1
    for i, _ in enumerate(last_results or []):
        percent = int((i + 1) / total * 100)
        progress_var.set(percent)
        root.update_idletasks()

    display_results(last_results)

# ======================================= email validation =======================================================================

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# ======================================= display results in Tkinter tree =========================================================

def display_results(results):
    for item in tree.get_children():
        tree.delete(item)
    for row in results or []:
        tree.insert("", "end", values=(
            row.get("name", ""),
            row.get("url", ""),
            row.get("status", "")
        ))

    # Update both labels
    count = len(results) if results else 0
    count_label.config(text=f"Accounts found: {count}")
    status_label.config(text="Search complete")

# ======================================= clickable hyperlinks =====================================================================

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

# ======================================= export results to PDF =====================================================================

def export_results_to_pdf():
    global last_results, last_mode, last_phrase, search_results_by_phrase
    if not last_results:
        messagebox.showwarning("No Results", "There are no results to export.")
        return

    # Default filename suggestion
    default_name = f"blackbird_results_{last_mode}.pdf"

    filename = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save Results as PDF",
        initialfile=default_name
    )
    if not filename:
        return

    try:
        c = pdf_canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        # Overall title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, f"Blackbird Search Results ({last_mode})")

        # Loop through each search phrase separately
        for phrase, results in search_results_by_phrase.items():
            # Start each phrase section on a new page
            c.showPage()
            y = height - 50

            # Section header
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y, f"Results for: {phrase}")
            y -= 30

            # Table headers
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, "Site")
            c.drawString(250, y, "URL")
            y -= 20

            # Table rows
            c.setFont("Helvetica", 10)
            for row in results:
                site = row.get("name", "")
                url = row.get("url", "")

                display_url = url if url else ""
                if len(display_url) > 60:
                    display_url = display_url[:57] + "..."

                c.drawString(50, y, site[:30])
                c.drawString(250, y, display_url)

                if url:
                    text_width = c.stringWidth(display_url, "Helvetica", 10)
                    c.linkURL(url, (250, y, 250 + text_width, y + 12), relative=0)

                y -= 20
                if y < 50:  # new page if space runs out
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 10)

        c.save()
        messagebox.showinfo("Export Successful", f"Results exported to {os.path.abspath(filename)}")
    except Exception as e:
        messagebox.showerror("Export Failed", f"An error occurred: {e}")


# ==================================================================================================================================
# ======================================= tkinter window setup =====================================================================
# ==================================================================================================================================

root = tk.Tk()
root.title("Blackbird GUI")
root.geometry("900x750")
root.resizable(False, False)

# ======================================= background image =========================================================================

bg_image = Image.open("blackbird.png")
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=900, height=750)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# ======================================= username =================================================================================

username_label = tk.Label(root, text="Usernames (comma separated):", bg="purple", fg="white") # <---------------------------------------------------   "Search Usernames" label (bg box, fg text)
username_entry = tk.Entry(root, width=50)
username_btn = tk.Button(root, text="Search Usernames", command=run_username_search, bg="red") # <--------------------------------------   "Search Usernames" button

canvas.create_window(100, 30, window=username_label, anchor="nw")
canvas.create_window(100, 55, window=username_entry, anchor="nw")
canvas.create_window(100, 85, window=username_btn, anchor="nw")

# ======================================= email ====================================================================================

email_label = tk.Label(root, text="Emails (comma separated):", bg="purple", fg="white") # <-------------------------------------------------   "Search Emails" label (bg box, fg text)
email_entry = tk.Entry(root, width=50)
email_btn = tk.Button(root, text="Search Emails", command=run_email_search, bg="red") # <------------------------------------------------   "Search Emails" button

canvas.create_window(100, 125, window=email_label, anchor="nw")
canvas.create_window(100, 150, window=email_entry, anchor="nw")
canvas.create_window(100, 180, window=email_btn, anchor="nw")

# ======================================= search options ============================================================================

options_label = tk.Label(root, text="Search Options:", bg="white")
canvas.create_window(100, 225, window=options_label, anchor="nw")

verbose_var = tk.BooleanVar()
permute_var = tk.BooleanVar()
permuteall_var = tk.BooleanVar()
no_nsfw_var = tk.BooleanVar()
filter_var = tk.BooleanVar()

canvas.create_window(100, 255, window=tk.Checkbutton(root, text="--verbose", variable=verbose_var, bg="white"), anchor="nw")
canvas.create_window(200, 255, window=tk.Checkbutton(root, text="--permute", variable=permute_var, bg="white"), anchor="nw")
canvas.create_window(300, 255, window=tk.Checkbutton(root, text="--permuteall", variable=permuteall_var, bg="white"), anchor="nw")
canvas.create_window(420, 255, window=tk.Checkbutton(root, text="--no-nsfw", variable=no_nsfw_var, bg="white"), anchor="nw")

custom_options_label = tk.Label(root, text="Custom Filter:", bg="white")
canvas.create_window(100, 295, window=custom_options_label, anchor="nw")
canvas.create_window(100, 320, window=tk.Checkbutton(root, text="--filter", variable=filter_var, bg="white"), anchor="nw")

filter_entry = tk.Entry(root, width=60)
filter_entry.insert(0, 'e.g. name=twitter or cat~social')
canvas.create_window(100, 345, window=filter_entry, anchor="nw")

# ======================================= progress bar and status ==================================================================

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
status_label = tk.Label(root, text="Idle", bg="white")

canvas.create_window(100, 410, window=progress_bar, anchor="nw", width=700)
canvas.create_window(100, 440, window=status_label, anchor="nw")

# ======================================= Count Label ==============================================================================

count_label = tk.Label(root, text="Accounts found: 0", bg="white")
canvas.create_window(100, 465, window=count_label, anchor="nw")

# ======================================= Table ====================================================================================

table_frame = tk.Frame(root)
canvas.create_window(100, 490, window=table_frame, anchor="nw", width=700, height=200)

scroll_y = tk.Scrollbar(table_frame, orient="vertical")
scroll_x = tk.Scrollbar(table_frame, orient="horizontal")

tree = ttk.Treeview(
    table_frame,
    columns=("Site", "URL", "Status"),
    show="headings",
    yscrollcommand=scroll_y.set,
)

tree.heading("Site", text="Site")
tree.column("Site", width=185, anchor="w")
tree.heading("URL", text="URL")
tree.column("URL", width=440, anchor="w")
tree.heading("Status", text="Status")
tree.column("Status", width=60, anchor="center")

scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)

scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
tree.pack(expand=True, fill="both")

tree.bind("<Double-1>", on_row_double_click)

# ======================================= Export Button ============================================================================

export_btn = tk.Button(root, text="Export to PDF", command=export_results_to_pdf, bg="red") # <-------------------------------------------------   "Export to PDF" button
canvas.create_window(100, 710, window=export_btn, anchor="nw")

# ======================================= Mainloop ================================================================================

root.mainloop()
