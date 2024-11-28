import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Engine import search

# def search(query, k, euclid):
#     # Simulate search result for demonstration
#     # You can replace this with your actual search logic
#     return [
#         {"title": f"Result {i+1} Title", "content": f"Content of result {i+1}"}
#         for i in range(int(k))
#     ]

def on_search():
    query = query_entry.get()
    k = result_entry.get()
    euclid = euclidean_var.get()

    # Validate k
    if not k.isdigit() and k:
        messagebox.showerror("Invalid Input", "'Number of Result' must be a number.")
        return
    if k:
        k = int(k)
    else:
        k = 5
    print(query)
    print(k)
    print(euclid)
    results = search(query.lower(), k, euclid)

    # Clear previous results
    for widget in results_frame.winfo_children():
        widget.destroy()

    # Display results
    for result in results:
        # Title and content with truncation if too long
        title_label = create_truncated_label(results_frame, f"Title: {result['Title']}", True)
        title_label.pack(anchor="w", pady=2)

        content_label = create_truncated_label(results_frame, f"Content: {result['Content']}")
        content_label.pack(anchor="w", pady=2)

def create_truncated_label(parent_frame, text, bold = False, width=100):
    # Create a label with text truncated if it exceeds the width
    truncated_text = text
    if len(text) > width:
        truncated_text = text[:width] + "..."
    if bold:
        label = tk.Label(parent_frame, text=truncated_text, font=("Arial", 10, "bold"))
    else:
        label = tk.Label(parent_frame, text=truncated_text, font=("Arial", 10))
    return label

# Main window
root = tk.Tk()
root.title("Search Engine")
root.geometry("800x600")

# Title label
title_label = tk.Label(root, text="Search Engine", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Query input
query_label = tk.Label(root, text="Query:", font=("Arial", 12))
query_label.pack(anchor="w", padx=10, pady=(10, 0))
query_entry = ttk.Entry(root, width=50)
query_entry.pack(padx=10, pady=5)

# Number of Result input
result_label = tk.Label(root, text="Number of Result:", font=("Arial", 12))
result_label.pack(anchor="w", padx=10, pady=(10, 0))
result_entry = ttk.Entry(root, width=20)
result_entry.pack(padx=10, pady=5)

# Euclidean checkbox
euclidean_var = tk.BooleanVar()
euclidean_checkbox = ttk.Checkbutton(root, text="Euclidean", variable=euclidean_var)
euclidean_checkbox.pack(anchor="w", padx=10, pady=5)

# Search button
search_button = ttk.Button(root, text="Search", command=on_search)
search_button.pack(pady=10)

# Frame to display results
results_frame = tk.Frame(root)
results_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Run the application
def run():
    root.mainloop()