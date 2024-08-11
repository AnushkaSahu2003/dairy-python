import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Directory to store diary entries
DIARY_DIR = "diary_entries"

# Ensure the diary directory exists
if not os.path.exists(DIARY_DIR):
    os.makedirs(DIARY_DIR)

def write_entry():
    date_str = datetime.now().strftime("%Y-%m-%d")
    entry = entry_text.get("1.0", tk.END).strip()
    
    if entry:
        file_name = f"{date_str}.txt"
        file_path = os.path.join(DIARY_DIR, file_name)
        
        with open(file_path, "a") as file:
            file.write(f"{datetime.now().strftime('%H:%M:%S')}\n{entry}\n\n")
        
        messagebox.showinfo("Success", "Entry saved!")
        entry_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Diary entry cannot be empty.")

def view_entry():
    date_str = date_entry.get()
    file_name = f"{date_str}.txt"
    file_path = os.path.join(DIARY_DIR, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.read()
            messagebox.showinfo(f"Entries for {date_str}", content)
    else:
        messagebox.showwarning("Warning", f"No entries found for {date_str}.")

def search_entries():
    keyword = search_entry.get().strip()
    found = False
    result_text = ""
    
    if keyword:
        for file_name in os.listdir(DIARY_DIR):
            file_path = os.path.join(DIARY_DIR, file_name)
            
            with open(file_path, "r") as file:
                content = file.read()
                if keyword.lower() in content.lower():
                    result_text += f"Keyword found in {file_name}:\n{content}\n"
                    found = True

        if found:
            result_box.delete("1.0", tk.END)
            result_box.insert(tk.END, result_text)
        else:
            messagebox.showinfo("Search Result", "No entries found with that keyword.")
    else:
        messagebox.showwarning("Warning", "Please enter a keyword to search.")

# Create the main window
root = tk.Tk()
root.title("Personal Diary Application")
root.geometry("500x600")

# Create and place the UI elements
tk.Label(root, text="Personal Diary Application", font=("Helvetica", 16)).pack(pady=10)

# Writing new entry
tk.Label(root, text="Write a new entry:").pack(anchor="w", padx=10, pady=5)
entry_text = scrolledtext.ScrolledText(root, width=60, height=10)
entry_text.pack(padx=10, pady=5)
tk.Button(root, text="Save Entry", command=write_entry).pack(pady=5)

# Viewing an entry
tk.Label(root, text="View an entry by date (YYYY-MM-DD):").pack(anchor="w", padx=10, pady=5)
date_entry = tk.Entry(root, width=20)
date_entry.pack(padx=10, pady=5)
tk.Button(root, text="View Entry", command=view_entry).pack(pady=5)

# Searching for entries
tk.Label(root, text="Search entries by keyword:").pack(anchor="w", padx=10, pady=5)
search_entry = tk.Entry(root, width=30)
search_entry.pack(padx=10, pady=5)
tk.Button(root, text="Search", command=search_entries).pack(pady=5)

# Display search results
tk.Label(root, text="Search Results:").pack(anchor="w", padx=10, pady=5)
result_box = scrolledtext.ScrolledText(root, width=60, height=10)
result_box.pack(padx=10, pady=5)

# Run the application
root.mainloop()
